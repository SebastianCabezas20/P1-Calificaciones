<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSectionV2">
        <h3 class="textTitleV2">Solicitudes de apelación</h3>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th style="width: 20%">Curso</th>
            <th style="width: 10%;">Evaluación</th>
            <th style="width: 10%;">Estado</th>
            <th style="width: 25%;">Motivo</th>
            <th style="width: 25%;">Respuesta</th>
            <th style="width: 3%;"></th>
            <th style="width: 4%;"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="solicitud in solicitudes" :key="solicitud.id">
            <Solicitudes :solicitud="solicitud" 
              @EventModificarSolicitud = "(solicitud) => abrirModificarSolicitud(solicitud)"
              @EventMostrarSeguimiento = "(solicitud) => mostrarSeguimiento(solicitud)"
            />
          </tr>

          <transition name="fase" appear>
            <div class="modal-overlay" v-if="showModalModificacion">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title">Modificar motivo de solicitud</h5>
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                      @click="showModalModificacion = false"
                    ></button>
                  </div>
                  
                  <div class="modal-body">
                    <form 
                      action="#"
                      method="PUT"
                      v-on:submit.prevent="
                        modificarSolicitud()
                      ">
                      <div class="mb-3">
                        <label class="form-label">Motivo del cambio</label>
                        <textarea
                          v-model="nuevoMotivo"
                          class="form-control"
                          rows="7"
                          placeholder="Ingrese el motivo del cambio"
                          required
                        ></textarea>
                      </div>
                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-secondary"
                          data-bs-dismiss="modal"
                          @click="showModalModificacion = false"
                        >
                          Cerrar
                        </button>
                        <button type="submit" class="btn btn-primary">
                          Guardar cambios
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
        </transition>

        <transition name="fase" appear>
          <div class="modal-overlay" v-if="showTrack" :data="solicitud">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Seguimiento de solicitud</h5>
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                    @click="showTrack = false"
                  ></button>
                </div>
                <div class="modal-body">
                  <div class="row">
                    <div class="col-12 pt-1 pb-1">
                      <div class="row justify-content-between">
                        <div class="track completed">
                          <span class="is-complete"></span>
                          <p>
                            Enviado<br /><span
                              >La solicitud de revisión fue enviada
                              satisfactoriamente el día {{solicitud.fecha_creacion}}</span
                            >
                          </p>
                        </div>
      
                        <!-- Segundo paso. -->
                        <div v-if="solicitud.estado == 'P'" class="track">
                          <span class="is-complete"></span>
                          <p>
                            En revisión<br /><span
                              >La o él docente se encuentra revisando la
                              solicitud</span
                            >
                          </p>
                        </div>
                        <div v-else class="track completed">
                          <span class="is-complete"></span>
                          <p>
                            En revisión<br /><span
                              >La o él docente se encuentra revisando la
                              solicitud</span
                            >
                          </p>
                        </div>
      
                        <!-- Último paso. -->
                        <!-- Se verifica si la solicitud fue aprobada o rechazada.-->
                        <div v-if="solicitud.estado == 'R'" class="track rejected">
                          <span class="is-complete"></span>
                          <p>
                            Rechazada<br /><span
                              >Su solicitud de revisión fue rechazada y su
                              calificación se mantiene</span
                            >
                          </p>
                        </div>
      
                        <div
                          v-else-if="solicitud.estado == 'A'"
                          class="track completed"
                        >
                          <span class="is-complete"></span>
                          <p>
                            Aprobada<br /><span
                              >Su solicitud de revisión fue aprobada y su calificación
                              ya se encuentra actualizada</span
                            >
                          </p>
                        </div>
      
                        <div v-else class="track">
                          <span class="is-complete"></span>
                          <p>
                            Respuesta<br /><span
                              >La o él docente aprueba o rechaza la solicitud de
                              revisión enviada</span
                            >
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-secondary"
                    data-bs-dismiss="modal"
                    @click="showTrack = false"
                  >
                    Cerrar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </transition>
        </tbody>
      </table>

      <div class="informacionAdicional">
        <p>*Usted puede modificar el motivo de sus solicitudes de revisión únicamente si estas se encuentran en el estado de "Pendiente"</p>
      </div>

    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import Solicitudes from "../../components/Solicitud.vue";
import axios from "axios";

export default {
  data() {
    return {
      solicitudes: [],
      solicitud: null,
      nuevoMotivo: '',
      showModalModificacion: false,
      showTrack: false,
    };
  },
  components: {
    Sidebar,
    Navbar,
    Solicitudes,
  },
  mounted() {
    let ins = this;
    let idUsuarioLogeado = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/solicitudes/${idUsuarioLogeado}`)
      .then(function (response) {
        ins.solicitudes = response.data;
      });
  },
  methods: {
    abrirModificarSolicitud(solicitud){
      this.solicitud = solicitud;
      this.nuevoMotivo = solicitud.motivo;
      this.showModalModificacion = true;
    },

    mostrarSeguimiento(solicitud) {
      this.solicitud = solicitud;
      this.showTrack = true;
    },

    modificarSolicitud(){
      let that = this;      
      this.$swal
        .fire({
          title: "¿Está seguro de cambiar el motivo de su solicitud de revisión?",
          showDenyButton: true,
          showCancelButton: true,
          cancelButtonText: "Cancelar",
          confirmButtonText: "Guardar",
          denyButtonText: "No guardar",
        }).then((result) => {
          if(result.isConfirmed) {
            this.solicitud['motivo'] = this.nuevoMotivo;

            let solicitudActualizada = {
              motivo: this.nuevoMotivo,
              anterior_nota: this.solicitud.anterior_nota,
              actual_nota: this.solicitud.actual_nota,
              fecha_creacion: this.solicitud.fecha_creacion,
              archivoAdjunto: this.solicitud.archivoAdjunto,
              respuesta: this.solicitud.respuesta,
              fecha_respuesta: this.solicitud.fecha_respuesta,
              estado: this.solicitud.estado,
              id_estudiante: this.solicitud.id_estudiante.id,
              id_docente: this.solicitud.id_docente.id,
              id_evaluacion: this.solicitud.id_evaluacion.id,
              id_calificacion: this.solicitud.id_calificacion.id,
            };

            axios
              .put(`http://localhost:8000/actualizar/solicitud/${this.solicitud.id}`, solicitudActualizada)
              .then(function (response) {
                that.$swal.fire({
                      icon: "success",
                      title: "Modificación exitosa",
                      text: `La solicitud de revisión fue modificada satisfactoriamente`,
                    });
                that.showModalModificacion = false;
              });
          }
          else {
            this.$swal.fire("Los cambios no fueron efectuados", "", "info");
            this.showModalModificacion = false;
          }
        });
    }
  },
};
</script>

<style></style>
