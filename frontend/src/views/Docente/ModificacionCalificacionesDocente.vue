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
        <h3 class="textTitleV2">Calificaciones</h3>
      </div>

      <!-- Modificar el diseño con el que se muestra la información, por algo mas moderno. -->
      <div class="row" style="background-color: #ffffff">
        <div class="col-sm-8 p-0">
          <p class="informationCalification">
            Nombre: {{ this.informacionEvaluacion.nombre }}
          </p>

          <p
            v-if="this.informacionEvaluacion.estado == 'P'"
            class="informationCalification"
          >
            Estado: Pendiente
          </p>
          <p v-else class="informationCalification">Estado: Evaluada</p>

          <p class="informationCalification">
            Fecha de realización:
            {{ this.informacionEvaluacion.fechaEvActual }}
          </p>
        </div>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>RUT</th>
            <th>D. Verificador</th>
            <th>Calificación</th>
            <th>Modificar Calificación</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(calificacion, index) in calificaciones" :key="index">
            <td>{{ calificacion.id_estudiante.id_usuario.first_name }}</td>
            <td>{{ calificacion.id_estudiante.id_usuario.last_name }}</td>
            <td>{{ calificacion.id_estudiante.rut }}</td>
            <td>{{ calificacion.id_estudiante.dig_verificador }}</td>
            <td>{{ calificacion.nota }}</td>
            <td>
              <div>
                <button
                  @click="(showModal = true), (modalIndex = index)"
                  class="fa-solid fa-pencil botonTabla"
                  title="Modificar calificación"
                ></button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Modal Modificar Fecha-->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModal">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Modificar Calificación</h5>
                <button
                  type="button"
                  class="btn-close"
                  @click="showModal = false"
                ></button>
              </div>

              <div class="modal-body">
                <form
                  action="#"
                  method="PUT"
                  v-on:submit.prevent="
                    modificarCalificacion($event, modalIndex)
                  "
                >
                  <div class="mb-3">
                    <label class="form-label">Nueva calificación</label>
                    <input
                      v-model="nuevaCalificacion"
                      class="form-control"
                      type="number"
                      placeholder="Nueva calificación del estudiante"
                      min="1"
                      max="7"
                      step="0.1"
                      required
                    />
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Motivo del cambio</label>
                    <textarea
                      v-model="motivoCambio"
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
                      v-on:click="showModal = false"
                    >
                      Cancelar
                    </button>
                    <button type="submit" class="btn btn-primary">
                      Guardar Cambios
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";

export default {
  props: ["idEvaluacion", "idCurso"],

  components: {
    Sidebar,
    Navbar,
  },

  data() {
    return {
      calificaciones: [],
      informacionEvaluacion: [],
      showModal: false,
      indexModal: "",
      nuevaCalificacion: "",
      motivoCambio: "",
    };
  },
  mounted() {
    let identificacionEvaluacion = this.idEvaluacion;
    let ins = this;
    axios
      .get(
        `http://localhost:8000/calificacionesDocente/${identificacionEvaluacion}`
      )
      .then(function (response) {
        ins.calificaciones = response.data;
      });
    axios
      .get(`http://localhost:8000/evaluacion/${identificacionEvaluacion}`)
      .then(function (response) {
        ins.informacionEvaluacion = response.data;
      });
  },
  methods: {
    modificarCalificacion: function (event, index) {
      // Variables necesarias en los requests.
      let that = this;
      let idCalificacionModificar = this.calificaciones[index].id;

      // Variables que almacenan algunos datos del estudiante.
      let nombreEstudiante =
        this.calificaciones[index].id_estudiante.id_usuario.first_name;
      let apellidoEstudiante =
        this.calificaciones[index].id_estudiante.id_usuario.last_name;

      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);

      let nuevaCalificacion = {
        nota: this.nuevaCalificacion,
        fecha_entrega: this.calificaciones[index].fecha_entrega,
        obs_privada: this.calificaciones[index].obs_privada,
        id_estudiante: this.calificaciones[index].id_estudiante.id,
        id_evaluacion: this.calificaciones[index].id_evaluacion.id,
      };
      let cambioNota = {
        anterior_nota: this.calificaciones[index].nota,
        actual_nota: this.nuevaCalificacion,
        fecha_cambio: fechaActual,
        motivo: this.motivoCambio,
        id_calificacion: idCalificacionModificar,
      };

      axios
        .put(
          `http://localhost:8000/updateCalificacion/${idCalificacionModificar}`,
          nuevaCalificacion
        )
        .then(function (response) {
          axios
            .post("http://localhost:8000/add/cambio/calificacion", cambioNota)
            .then(function (responseTwo) {
              that.$swal
                .fire({
                  icon: "success",
                  title: "Modificación exitosa",
                  text: `La calificación de ${nombreEstudiante} ${apellidoEstudiante} fue modificada satisfactoriamente`,
                })
                .then((result) => {
                  location.reload();
                });
            });
        });
    },
  },
};
</script>

<style></style>
