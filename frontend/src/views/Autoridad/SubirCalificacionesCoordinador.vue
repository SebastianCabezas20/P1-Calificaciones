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
        <h3 class="textTitleV2">Calificación de Estudiantes</h3>
      </div>

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
          <p class="informationCalification">
            Fecha límite de entrega de notas:
            {{ this.informacionEvaluacion.fechaEntrega }}
          </p>
        </div>

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

      <form @submit.prevent="submitCalificaciones" action="POST">
        <table class="tableV2">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>RUT</th>
              <th>D. Verificador</th>
              <th>Calificación</th>
              <th style="width: 10%"></th>
              <th class="row-ButtonIcon"></th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="(calificacion, index) in calificacionesEstudiantes"
              :key="calificacion.id"
            >
              <td>
                {{ calificacion.id_estudiante.id_usuario.first_name }}
              </td>
              <td>
                {{ calificacion.id_estudiante.id_usuario.last_name }}
              </td>
              <td>
                {{ calificacion.id_estudiante.rut }}
              </td>
              <td>
                {{ calificacion.id_estudiante.dig_verificador }}
              </td>
              <td v-if="calificacion.nota == null || calificacion.nota == ''">
                -
              </td>
              <td v-else>{{ calificacion.nota }}</td>

              <td>
                <input
                  class="form-control text-center"
                  type="number"
                  min="1"
                  max="7"
                  step="0.1"
                  placeholder="Calificación"
                  required
                  v-model="calificacionesEstudiantes[index].nota"
                />
              </td>
              <td>
                <div class="text-center">
                  <button
                    class="fa-solid fa-plus botonTabla"
                    type="button"
                    v-on:click="addObsPrivada($event, index)"
                  ></button>
                </div>
              </td>

              <!-- Modal qde subida de observaciones privada a una evaluación. -->
              <transition name="fase" appear>
                <div
                  class="modal-overlay"
                  v-if="showModalObservacionPrivada"
                  :data="modalData"
                >
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title">Observación privada</h5>
                        <button
                          type="button"
                          class="btn-close"
                          @click="showModalObservacionPrivada = false"
                        ></button>
                      </div>
                      <div class="modal-body">
                        <div class="mb-3">
                          <label for="contenidoObservacion"
                            >Indique una observación privada</label
                          >
                          <textarea
                            name="contenidoObservacionPrivada"
                            id="contenidoObservacionPrivada"
                            rows="5"
                            type="text"
                            v-model="
                              calificacionesEstudiantes[modalData].obs_privada
                            "
                            class="form-control"
                            placeholder="Contenido de la observación"
                          ></textarea>
                        </div>

                        <div class="modal-footer">
                          <button
                            type="button"
                            class="btn btn-primary"
                            v-on:click="showModalObservacionPrivada = false"
                          >
                            Guardar cambios
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </transition>
            </tr>
          </tbody>
        </table>

        <!-- Botón  observación general (Opcional). -->
        <div class="pb-3">
          <button
            @click="showModalObservacion = true"
            type="button"
            class="buttonSecondary"
          >
            Agregar observación
          </button>
        </div>

        <!-- Botón para subir las calificaciones  -->
        <div>
          <button type="submit" class="submitButton">
            Subir calificaciones
          </button>
        </div>
      </form>

      <!-- Modal que permite la subida de observaciones generales a una evaluación. -->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModalObservacion">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Observación general</h5>
                <button
                  type="button"
                  class="btn-close"
                  @click="showModalObservacion = false"
                ></button>
              </div>
              <div class="modal-body">
                <div class="mb-3">
                  <label for="contenidoObservacion"
                    >Indique una observación general</label
                  >
                  <textarea
                    name="contenidoObservacion"
                    id="contenidoObservacion"
                    rows="5"
                    type="text"
                    v-model="contenidoObservacion"
                    class="form-control"
                    placeholder="Contenido de la observación"
                  ></textarea>
                </div>

                <!-- Subir un archivo adjunto a una evaluación (Sprint 3). -->
                <div class="mb-3">
                  <label for="formFile" class="form-label"
                    >Adjuntar archivo</label
                  >
                  <input class="form-control" type="file" id="formFile" />
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-primary"
                    v-on:click="showModalObservacion = false"
                  >
                    Finalizar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import * as XLSX from "xlsx";
import axios from "axios";

export default {
  props: ["idEvaluacion", "idCurso"],
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      calificacionesEstudiantes: [],
      estudiantesPlanilla: [],
      calificaciones: [],
      contenidoObservacion: "",
      informacionEvaluacion: [],
      showModalObservacion: false,
      showModalObservacionPrivada: false,
      modalData: null,
    };
  },
  mounted() {
    let identificacionEvaluacion = this.idEvaluacion;
    let identificacionCurso = this.idCurso;
    let ins = this;
    axios
      .get(
        `http://localhost:8000/calificacion/coordinacion/${identificacionCurso}`
      )
      .then(function (response) {
        ins.calificacionesEstudiantes = response.data;
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
          
          // Carga de datos en la tabla.
          for (var i = 0; i < that.calificacionesEstudiantes.length; i++) {
            for (var j = 0; j < data.length; j++) {
              if (
                that.calificacionesEstudiantes[i].id_estudiante.rut ==
                  data[j][0] &&
                that.calificacionesEstudiantes[i].id_estudiante
                  .dig_verificador == data[j][1]
              ) {
                that.calificacionesEstudiantes[i].nota = data[j][2];
                contadorCarga++;
              }
            }
          }

          // Caso 1: Todas las filas del archivo se cargaron.
          if (contadorCarga == data.length) {
            that.$swal.fire({
              icon: "success",
              title: "Carga de calificaciones exitosa",
              text: "La planilla de calificaciones fue cargada satisfactoriamente",
            });
          }

          // Caso 2: El archivo adjunto no sigue el formato.
          else if (contadorCarga == 0) {
            that.$swal.fire({
              icon: "error",
              title: "Carga de calificaciones fallida",
              text: "La planilla de calificaciones adjunta no corresponde al formato requerido, por lo tanto, no se realizó la carga de calificaciones correctamente.",
            });
          }
          
          // Caso 3: Algunas filas del archivo no se cargaron.
          else {
            that.$swal.fire({
              icon: "info",
              title: "Subida de calificaciones exitosa con observaciones",
              text: "La planilla de calificaciones fue cargada satisfactoriamente, sin embargo, algunos estudiantes de la planilla no coincidian con los estudiantes matriculados en la sección actual.",
            });
          }
        };
        reader.readAsArrayBuffer(this.file);
      }
    },

    addObsPrivada(event, index) {
      this.modalData = index;
      this.showModalObservacionPrivada = true;
    },

    submitCalificaciones() {
      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);
      let nuevaCalificacion;
      let that = this;

      for (var i = 0; i < this.calificacionesEstudiantes.length; i++) {
        nuevaCalificacion = {
          nombre: this.calificacionesEstudiantes[i].id_estudiante.rut,
          nota: this.calificacionesEstudiantes[i].nota,
          fecha_entrega: fechaActual,
          obs_privada: this.calificacionesEstudiantes[i].obs_privada,
          id_estudiante: this.calificacionesEstudiantes[i].id_estudiante.id,
          id_evaluacion: this.idEvaluacion,
        };
        axios
          .post("http://localhost:8000/add/calificacion", nuevaCalificacion)
          .then(function (response) {});
      }

      let nuevaEvaluacion = {
        nombre: this.informacionEvaluacion.nombre,
        fechaEvActual: this.informacionEvaluacion.fechaEvActual,
        fechaEntrega: this.informacionEvaluacion.fechaEntrega,
        ponderacion: this.informacionEvaluacion.ponderacion,
        estado: "E",
        obs_general: this.contenidoObservacion,
        adjunto: this.informacionEvaluacion.adjunto,
        id_tipoEvaluacion: this.informacionEvaluacion.id_tipoEvaluacion,
        id_docente: this.informacionEvaluacion.id_docente,
        id_coordinacion: this.informacionEvaluacion.id_coordinacion,
      };
      axios
        .put(
          `http://localhost:8000/update/evaluacion/${this.idEvaluacion}`,
          nuevaEvaluacion
        )
        .then(function (response) {
          that.$swal
            .fire({
              icon: "success",
              title: "Calificación exitosa",
              text: "Los estudiantes fueron calificados satisfactoriamente",
            })
            .then((result) => {
              that.$router.push({ path: `/coordinador/asignaturas/general` });
            });
        });
    },
  },
};
</script>

<style></style>
