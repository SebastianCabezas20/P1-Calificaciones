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

        <!-- Subida de planilla para la modificación automática. -->
        <div class="col-sm-4">
          <label for="formFile" class="form-label">Adjuntar planilla</label>
          <input
            class="form-control"
            type="file"
            id="formFile"
            @change="onChange"
          />
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
              <div
                v-if="
                  calificacion.notaNueva == null || calificacion.notaNueva == ''
                "
              >
                <button
                  v-on:click="addCambioNota($event, index)"
                  class="fa-solid fa-pencil botonTabla"
                  title="Modificar calificación"
                ></button>
              </div>
              <div v-else>
                <button
                  v-on:click="addCambioNota($event, index)"
                  class="fa-solid fa-pencil botonTabla"
                  title="Modificar calificación"
                  style="background-color: #f38a24"
                ></button>
              </div>
            </td>
          </tr>

          <!-- Modal Modificar Calificación-->
          <transition name="fase" appear>
            <div class="modal-overlay" v-if="showModal" :data="modalData">
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
                        modificarCalificacion($event, modalData)
                      "
                    >
                      <div class="mb-3">
                        <label class="form-label">Nueva calificación</label>
                        <input
                          v-model="calificaciones[modalData].notaNueva"
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
                          v-model="calificaciones[modalData].motivoCambio"
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
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import * as XLSX from "xlsx";

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
      modalData: null,
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
    onChange(event) {
      this.file = event.target.files ? event.target.files[0] : null;

      if (this.file) {
        const reader = new FileReader();
        let that = this;
        reader.onload = function (e) {
          /* Analizar el excel */
          const bstr = e.target.result;
          const wb = XLSX.read(bstr, { type: "array" });

          /* Obtener primera hoja. */
          const wsname = wb.SheetNames[0];
          const ws = wb.Sheets[wsname];

          /* Convertir los datos en un arreglo de arreglos. */
          const data = XLSX.utils.sheet_to_json(ws, {
            header: 1,
            range: 1,
          });

          let contadorCarga = 0;

          // Carga de datos.
          for (var i = 0; i < that.calificaciones.length; i++) {
            for (var j = 0; j < data.length; j++) {
              if (
                that.calificaciones[i].id_estudiante.rut == data[j][0] &&
                that.calificaciones[i].id_estudiante.dig_verificador ==
                  data[j][1]
              ) {
                that.calificaciones[i].notaNueva = data[j][2];
                that.calificaciones[i].motivoCambio = data[j][3];
                contadorCarga++;
              }
            }
          }

          // Caso 1: Todas las filas del archivo se cargaron.
          if (contadorCarga == data.length) {
            that.$swal.fire({
              icon: "success",
              title: "Carga de calificaciones exitosa",
              text: "La planilla de nuevas calificaciones fue cargada satisfactoriamente",
            });
          }

          // Caso 2: El archivo adjunto no sigue el formato.
          else if (contadorCarga == 0) {
            that.$swal.fire({
              icon: "error",
              title: "Carga de calificaciones fallida",
              text: "La planilla de nuevas calificaciones no contiene el formato requerido.",
            });
          }

          // Caso 3: Algunas filas del archivo no se cargaron.
          else {
            that.$swal.fire({
              icon: "info",
              title:
                "Subida de nuevas calificaciones exitosa con observaciones",
              text: "La planilla de nuevas calificaciones fue cargada satisfactoriamente, sin embargo, algunos estudiantes de la planilla no coincidian con los estudiantes matriculados en la sección actual.",
            });
          }
        };
        reader.readAsArrayBuffer(this.file);
      }
    },

    addCambioNota(event, index) {
      this.modalData = index;
      this.showModal = true;
    },

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

      this.$swal
        .fire({
          title: `Está seguro de cambiar la calificación a ${nombreEstudiante} ${apellidoEstudiante}?`,
          showDenyButton: true,
          showCancelButton: true,
          cancelButtonText: "Cancelar",
          confirmButtonText: "Guardar",
          denyButtonText: "No guardar",
        })
        .then((result) => {
          /* Docente está seguro de cambiar la calificación. */
          if (result.isConfirmed) {
            let nuevaCalificacion = {
              nota: this.calificaciones[index].notaNueva,
              fecha_entrega: this.calificaciones[index].fecha_entrega,
              obs_privada: this.calificaciones[index].obs_privada,
              adjunto: this.calificaciones[index].adjunto,
              id_estudiante: this.calificaciones[index].id_estudiante.id,
              id_evaluacion: this.calificaciones[index].id_evaluacion.id,
            };
            let cambioNota = {
              anterior_nota: this.calificaciones[index].nota,
              actual_nota: this.calificaciones[index].notaNueva,
              fecha_cambio: fechaActual,
              motivo: this.calificaciones[index].motivoCambio,
              id_calificacion: idCalificacionModificar,
            };

            axios
              .put(
                `http://localhost:8000/updateCalificacion/${idCalificacionModificar}`,
                nuevaCalificacion
              )
              .then(function (response) {
                axios
                  .post(
                    "http://localhost:8000/add/cambio/calificacion",
                    cambioNota
                  )
                  .then(function (responseTwo) {
                    that.$swal.fire({
                      icon: "success",
                      title: "Modificación exitosa",
                      text: `La calificación de ${nombreEstudiante} ${apellidoEstudiante} fue modificada satisfactoriamente`,
                    });

                    // Se actualizan los campos de aquella calificación para
                    // mostrarlos actualizados en la vista
                    that.calificaciones[index].nota =
                      that.calificaciones[index].notaNueva;
                    that.calificaciones[index].notaNueva = null;
                    that.calificaciones[index].motivoCambio = null;

                    that.showModal = false;
                  });
              });
          } else if (result.isDenied) {
            this.$swal.fire("Los cambios no fueron efectuados", "", "info");
            this.showModal = false;
          }
        });
    },
  },
};
</script>

<style></style>
