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
        <h3 class="textTitleV2">Calificación de estudiantes</h3>
      </div>

      <!-- Modificar el diseño con el que se muestra la información, por algo mas moderno. -->
      <div class="row" style="background-color: #ffffff">
        <div class="col-sm-8 p-0">
          <p class="informationCalification">
            Nombre: {{ this.informacionEvaluacion[0].nombre }}
          </p>

          <p
            v-if="this.informacionEvaluacion[0].estado == 'P'"
            class="informationCalification"
          >
            Estado: Pendiente
          </p>
          <p v-else class="informationCalification">Estado: Evaluada</p>

          <p class="informationCalification">
            Fecha de realización:
            {{ this.informacionEvaluacion[0].fechaEvActual }}
          </p>
          <p class="informationCalification">
            Fecha límite de entrega de notas:
            {{ this.informacionEvaluacion[0].fechaEntrega }}
          </p>
        </div>

        <div class="col-sm-4">
          <label for="formFile" class="form-label"
            >Adjuntar planilla (formato .xlsx)</label
          >
          <input
            class="form-control"
            type="file"
            id="formFile"
            @change="onChange"
          />
        </div>
      </div>

      <form
        @submit.prevent="submitCalificaciones"
        action="POST"
        enctype="multipart/form-data"
      >
        <table class="tableV2">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>RUT</th>
              <th>D. Verificador</th>
              <th style="width: 10%">Calificación</th>
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

              <td>
                <input
                  class="form-control text-center"
                  type="number"
                  min="1"
                  max="7"
                  step="0.1"
                  placeholder="Calificación"
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
            </tr>

            <!-- Modal que permite la subida de observaciones privada a una evaluación. -->
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

                      <div class="mb-3">
                        <label for="formFile" class="form-label"
                          >Adjuntar archivo</label
                        >
                        <input
                          class="form-control"
                          type="file"
                          id="formFile"
                          @change="subirArchivoPrivado($event, modalData)"
                        />
                        <p v-if="calificacionesEstudiantes[modalData].adjunto">
                          Archivo guardado:
                          {{
                            calificacionesEstudiantes[modalData].adjunto.name
                          }}
                        </p>
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
          </tbody>
        </table>

        <!-- Botón para agregar una observación general (Opcional). -->
        <div class="pb-3">
          <button
            @click="showModalObservacion = true"
            type="button"
            class="buttonSecondary"
          >
            Agregar observación
          </button>
        </div>

        <!-- Botón para subir las calificaciones 
          (Se debe tener calificación para cada estudiante) -->
        <div>
          <button type="submit" class="submitButton">
            Subir calificaciones
          </button>
        </div>

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

                  <div class="mb-3">
                    <label for="formFile" class="form-label"
                      >Adjuntar archivo</label
                    >
                    <input
                      class="form-control"
                      type="file"
                      id="formFile"
                      @change="subirArchivoGeneral($event)"
                    />
                    <p v-if="archivoGeneral !== null">
                      Archivo guardado: {{ archivoGeneral.name }}
                    </p>
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
      </form>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import * as XLSX from "xlsx";
import axios from "axios";
import emailjs from 'emailjs-com';

export default {
  props: ["nombreEvaluacion", "idCurso","idDocente"],
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
      archivoGeneral: null,
    };
  },
  created() {
    let identificacionEvaluacion = this.nombreEvaluacion;
    let identificacionCurso = this.idCurso; // Horario
    let identificacionDocente = this.idDocente;
    let ins = this;
    axios
      .get(
        `http://localhost:8000/calificacion/coordinacion/${identificacionCurso}/${identificacionDocente}/CE`
      )
      .then(function (response) {
        ins.calificacionesEstudiantes = response.data;
      });
    axios
      .get(`http://localhost:8000/evaluacion/${identificacionEvaluacion}/${identificacionCurso}/${identificacionDocente}/CE`)
      .then(function (response) {
        ins.informacionEvaluacion = response.data;
        console.log(ins.informacionEvaluacion)
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
          let calificacionesErroneas = 0;

          // Comprobación de errores.
          for (var i = 0; i < data.length; i++) {
            // Calificación es mayor que 7 y menor que 1.
            if (Number(data[i][2]) && (data[i][2] < 1 || data[i][2] > 7)) {
              calificacionesErroneas++;
            }
            // Calificación tiene más de un decimal.
            else if (
              Number(data[i][2]) &&
              data[i][2] % 1 !== 0 &&
              String(data[i][2]).split(".")[1].length !== 1
            ) {
              calificacionesErroneas++;
            }
          }

          // Caso 1: Archivo no tiene errores en las calificaciones.
          if (calificacionesErroneas == 0) {
            // Carga de datos en la tabla.
            for (var i = 0; i < that.calificacionesEstudiantes.length; i++) {
              for (var j = 0; j < data.length; j++) {
                if (
                  that.calificacionesEstudiantes[i].id_estudiante.rut ==
                    data[j][0] &&
                  that.calificacionesEstudiantes[i].id_estudiante
                    .dig_verificador == data[j][1] &&
                  Number(data[j][2])
                ) {
                  that.calificacionesEstudiantes[i].nota = data[j][2];
                  contadorCarga++;
                }
              }
            }

            // Caso 1: Todas las filas del archivo se cargaron.
            if (
              contadorCarga == data.length &&
              contadorCarga == that.calificacionesEstudiantes.length
            ) {
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
                text: "La planilla de calificaciones fue cargada satisfactoriamente, sin embargo, algunos estudiantes de la planilla no coincidian con los estudiantes matriculados en la sección actual o viceversa.",
              });
            }
          } else {
            that.$swal.fire({
              icon: "error",
              title: "Carga de calificaciones fallida",
              text: "La planilla de calificaciones adjunta no corresponde al formato requerido, por lo tanto, no se realizó la carga de calificaciones correctamente.",
            });
          }
        };
        reader.readAsArrayBuffer(this.file);
      }
    },

    subirArchivoPrivado(event, index) {
      this.calificacionesEstudiantes[index].adjunto = event.target.files[0];
    },

    subirArchivoGeneral(event) {
      this.archivoGeneral = event.target.files[0];
    },

    addObsPrivada(event, index) {
      this.modalData = index;
      this.showModalObservacionPrivada = true;
    },

    submitCalificaciones() {
      /* Modificación de los encabezados de los request, puesto que se envían
      archivos. */
      let axiosConfig = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      /* Docente no ingresa la nota de un estudiante. En este caso se le obliga
      al docente a ingresar una observación privada para indicar el motivo. 
      Para esto se verifican las calificaciones no ingresadas y se comprueba si
      tales estudiantes no recibieron una observación privada.*/
      for(var i = 0; i < this.calificacionesEstudiantes.length; i++) {
        if (this.calificacionesEstudiantes[i].nota === '' || this.calificacionesEstudiantes[i].nota === undefined) {
          if (this.calificacionesEstudiantes[i].obs_privada === '' || this.calificacionesEstudiantes[i].obs_privada === undefined) {
            this.$swal.fire({
              icon: 'error',
              title: 'Error',
              text: `El(la) estudiante ${this.calificacionesEstudiantes[i].id_estudiante.id_usuario.first_name + " " + this.calificacionesEstudiantes[i].id_estudiante.id_usuario.last_name} no recibió una calificación, por lo tanto, se solicita que le proporcione una observación privada para que conozca el motivo.`
            })
            return;
          }
        }
      }

      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);
      let nuevaCalificacion;
      let that = this;

      for (var i = 0; i < this.calificacionesEstudiantes.length; i++) {
        // Buscar el id_evaluacion correspondiente a ese estudiante segun el curso en que este inscrito
        let idEvaluacionEstudiante = 0
        for(var j = 0; j < this.informacionEvaluacion.length; j++){
          if(this.calificacionesEstudiantes[i].id_coordinacion.id == this.informacionEvaluacion[j].id_coordinacion){
            idEvaluacionEstudiante = this.informacionEvaluacion[j].id
          }
        }
        nuevaCalificacion = {
          nombre: this.calificacionesEstudiantes[i].id_estudiante.rut,
          nota: this.calificacionesEstudiantes[i].nota,
          fecha_entrega: fechaActual,
          obs_privada: this.calificacionesEstudiantes[i].obs_privada,
          adjunto: this.calificacionesEstudiantes[i].adjunto,
          id_estudiante: this.calificacionesEstudiantes[i].id_estudiante.id,
          id_evaluacion: idEvaluacionEstudiante,
        };
    
        axios
          .post(
            "http://localhost:8000/add/calificacion",
            nuevaCalificacion,
            axiosConfig
          )
          .then(function (response) {});
      }

      //Envío de mail a todos los estudiantes que fueron calificados.
      for (var i = 0; i < this.calificacionesEstudiantes.length; i++) {
        emailjs.send('pingeso', 'template_nota', {
          nombre_curso: this.calificacionesEstudiantes[i].id_coordinacion.id_asignatura.nombre,
          nombre_estudiante: this.calificacionesEstudiantes[i].id_estudiante.id_usuario.first_name+" "+this.calificacionesEstudiantes[i].id_estudiante.id_usuario.last_name,
          nombre_evaluacion: this.nombreEvaluacion,
          mail_estudiante: this.calificacionesEstudiantes[i].id_estudiante.id_usuario.email
        },
        'TIAwArj4Go2oOAbqv')
        .then(function(response) {
          console.log('SUCCESS!', response.status, response.text);
        }, function(error) {
          console.log('FAILED...', error);
        });
      }

      for (var i = 0; i < this.informacionEvaluacion.length; i++){
        // Creacion de una evaluacion de una coordinacion en especifico para cursos espejo
        let nuevaEvaluacion = {
        nombre: this.informacionEvaluacion[i].nombre,
        fechaEvActual: this.informacionEvaluacion[i].fechaEvActual,
        fechaEntrega: this.informacionEvaluacion[i].fechaEntrega,
        ponderacion: this.informacionEvaluacion[i].ponderacion,
        estado: "E",
        obs_general: this.contenidoObservacion,
        adjunto: this.archivoGeneral,
        id_tipoEvaluacion: this.informacionEvaluacion[i].id_tipoEvaluacion,
        id_docente: this.informacionEvaluacion[i].id_docente,
        id_coordinacion: this.informacionEvaluacion[i].id_coordinacion,
        };
        axios
        .put(
          `http://localhost:8000/update/evaluacion/${this.informacionEvaluacion[i].id}`,
          nuevaEvaluacion,
          axiosConfig
        )
      }
      // revisar si aun funciona
      that.$swal
        .fire({
          icon: "success",
          title: "Calificación exitosa",
          text: "Los estudiantes fueron calificados satisfactoriamente",
        })
        .then((result) => {
          that.$router.push({ path: `/docente/curso/${that.idCurso}` });
        });
        
    },
  },
};
</script>

<style></style>
