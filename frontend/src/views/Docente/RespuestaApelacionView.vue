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
        <h4 class="textTitleV2">Responder apelación</h4>
      </div>

      <div class="d-flex align-middle justify-content-center mt-4">
        <div class="formApelacion" v-for="solicitud in apelacion.slice(0, 1)">
          <!-- Información de la solicitud. -->
          <div class="row" style="margin: 0px 0px 20px 0px; padding: 10px 0px">
            <div class="col" style="margin: 0px; padding: 0px">
              <h6 class="textoFormulario">
                Asignatura:
                {{
                  solicitud.id_evaluacion.id_coordinacion.id_asignatura.nombre
                }}
              </h6>
              <h6 class="textoFormulario">
                Código:
                {{
                  solicitud.id_evaluacion.id_coordinacion.id_asignatura.codigo
                }}-{{ solicitud.id_evaluacion.id_coordinacion.coordinacion }}-{{
                  solicitud.id_evaluacion.id_coordinacion.seccion
                }}
              </h6>
              <h6 class="textoFormulario">
                Evaluación: {{ solicitud.id_evaluacion.nombre }}
              </h6>
              <h6 class="textoFormulario">
                Calificación: {{ solicitud.id_calificacion.nota }}
              </h6>
            </div>
            <div class="col" style="display: flex; justify-content: end">
              <button
                class="buttonSecondary"
                type="button"
                @click="enRevision()"
                :disabled="solicitud.estado == 'E'"
              >
                Informar revisión
              </button>
            </div>
          </div>

          <form class="mt-2" @submit.prevent="send">
            <div class="itemFormulario">
              <label for="nombreUsuarioEstudiante">Estudiante</label>
              <input
                class="form-control relative block w-full"
                id="nombreUsuarioEstudiante"
                type="text"
                :value="solicitud.id_estudiante.id_usuario.username"
                disabled
                readonly
              />
            </div>

            <div class="itemFormulario">
              <label for="ApelacionContenido">Motivo de la apelación</label>
              <textarea
                class="form-control relative block w-full"
                id="ApelacionContenido"
                :value="solicitud.motivo"
                rows="4"
                disabled
                readonly
              >
              </textarea>
            </div>

            <div class="itemFormulario">
              <label for="Respuesta">Respuesta</label>
              <textarea
                class="form-control relative block w-full"
                id="ContenidoRespuesta"
                placeholder="Respuesta del docente"
                rows="5"
                v-model="respuestaActual"
                required
              ></textarea>
            </div>

            <div class="itemFormulario">
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="Estado"
                  id="RadioAceptar"
                  value="A"
                  v-model="EstadoActual"
                  @click="cambiarAceptado"
                />
                <label class="form-check-label" for="RadioAceptar">
                  Aceptar
                </label>
              </div>
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="Estado"
                  id="RadioRechazar"
                  v-model="EstadoActual"
                  value="R"
                  @click="cambiarRechazado"
                />
                <label class="form-check-label" for="RadioRechazar">
                  Rechazar
                </label>
              </div>
              <input
                type="number"
                v-model="notaActual"
                class="form-control relative"
                style="width: 180px"
                v-if="isAceptar"
                min="1"
                max="7"
                step="0.1"
                placeholder="Nueva calificación"
              />
            </div>

            <button class="submitButton" type="submit">Enviar Respuesta</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  props: ["idEstudiante", "idEvaluacion"],
  data() {
    return {
      apelacion: [],
      isAceptar: null,
      respuestaActual: "",
      notaActual: null,
      EstadoActual: "",
      idDocente: 0,
    };
  },
  methods: {
    cambiarRechazado() {
      this.isAceptar = false;
    },
    cambiarAceptado() {
      this.isAceptar = true;
    },
    send() {
      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);
      let idEstudianteSolicitud = this.idEstudiante;
      let idEvaluacionSolicitud = this.idEvaluacion;

      if (
        this.isAceptar == true &&
        (this.notaActual == null || this.notaActual == "")
      ) {
        this.$swal.fire({
          icon: "error",
          title: "No se pudo procesar la respuesta",
          text: "Para aceptar la solicitud de revisión, debe indicar la nueva nota del estudiante",
        });
      } else {
        // Caso 1: Solicitud es aceptada.
        if (this.isAceptar == true) {
          let solicitud = {
            motivo: this.apelacion[0].motivo,
            anterior_nota: this.apelacion[0].id_calificacion.nota, //Nota anterior
            actual_nota: this.notaActual, // Nueva nota
            fecha_creacion: this.apelacion[0].fecha_creacion,
            respuesta: this.respuestaActual,
            fecha_respuesta: fechaActual,
            estado: this.EstadoActual,
            id_estudiante: idEstudianteSolicitud,
            id_docente: this.apelacion[0].id_docente,
            id_evaluacion: idEvaluacionSolicitud,
            id_calificacion: this.apelacion[0].id_calificacion.id,
          };
          // ID de la solictud para actulizar
          let idSolicitud = this.apelacion[0].id;
          axios
            .put(
              `http://localhost:8000/actualizar/solicitud/${idSolicitud}`,
              solicitud
            )
            .then(function (response) {});

          // Nueva tupla de calificacion
          let notaNueva = {
            nota: this.notaActual,
            fecha_entrega: this.apelacion[0].id_calificacion.fecha_entrega,
            obs_privada: this.apelacion[0].id_calificacion.obs_privada,
            adjunto: this.apelacion[0].id_calificacion.adjunto,
            id_estudiante: this.apelacion[0].id_calificacion.id_estudiante,
            id_evaluacion: this.apelacion[0].id_calificacion.id_evaluacion,
          };
          let idCalificacion = this.apelacion[0].id_calificacion.id;

          axios
            .put(
              `http://localhost:8000/actualizar/calificacion/${idCalificacion}`,
              notaNueva
            )
            .then(function (response) {});
          // Se crea la tupla para el cambio de nota
          let cambioNota = {
            anterior_nota: this.apelacion[0].id_calificacion.nota,
            actual_nota: this.notaActual,
            fecha_cambio: fechaActual,
            motivo: this.respuestaActual,
            id_calificacion: this.apelacion[0].id_calificacion.id,
          };
          axios
            .post(`http://localhost:8000/add/cambio/calificacion`, cambioNota)
            .then(function (response) {
              router.push(`/docente/solicitudes/`);
            });
        }
        // Caso 2: Se rechaza la solicitud.
        else {
          let solicitud = {
            motivo: this.apelacion[0].motivo,
            anterior_nota: null, //Null debido a que no hubo cambio de nota
            actual_nota: this.apelacion[0].id_calificacion.nota, // Se mantiene la nota actual
            fecha_creacion: this.apelacion[0].fecha_creacion,
            respuesta: this.respuestaActual,
            fecha_respuesta: fechaActual,
            estado: this.EstadoActual,
            id_estudiante: idEstudianteSolicitud,
            id_docente: this.apelacion[0].id_docente,
            id_evaluacion: idEvaluacionSolicitud,
            id_calificacion: this.apelacion[0].id_calificacion.id,
          };
          // ID de la solictud para actulizar
          let idSolicitud = this.apelacion[0].id;
          axios
            .put(
              `http://localhost:8000/actualizar/solicitud/${idSolicitud}`,
              solicitud
            )
            .then(function (response) {
              router.push(`/docente/solicitudes/`);
            });
        }

        let solicitud = {
          id_estudiante: idEstudianteSolicitud,
          id_evaluacion: idEvaluacionSolicitud,
          motivo: this.apelacion[0].motivo,

          fecha_creacion: this.apelacion[0].fecha_creacion,
          respuesta: this.respuestaActual,
          fecha_respuesta: new Date(),
          estado: this.EstadoActual,
          id_docente: this.apelacion[0].id_docente,
        };
        let idSolicitud = this.apelacion[0].id;

        /// Actualizar solicitud con motivo, fecha de respuesta,etc
        axios
          .put(
            `http://localhost:8000/actualizar/solicitud/${idSolicitud}`,
            solicitud
          )
          .then(function (response) {});

        if (this.isAceptar == true) {
          if (this.notaActual != null) {
            let notaNueva = {
              nota: this.notaActual,
              fecha_entrega: this.notaJson[0].fecha_entrega,
              obs_privada: this.notaJson[0].obs_privada,
              adjunto: this.notaJson[0].adjunto,
              id_estudiante: this.notaJson[0].id_estudiante,
              id_evaluacion: this.notaJson[0].id_evaluacion,
            };
            let idCalificacion = this.notaJson[0].id;
            axios
              .put(
                `http://localhost:8000/actualizar/calificacion/${idCalificacion}`,
                notaNueva
              )
              .then(function (response) {});
            router.push(`/docente/solicitudes/`);
          } else {
            alert("ingrese una nota");
          }
        } else {
          router.push(`/docente/solicitudes/`);
        }
      }
    },
    enRevision() {
      let that = this;
      this.$swal
        .fire({
          title: "¿Desea informar la revisión de esta solicitud?",
          text: "En caso de informar la revisión, el estudiante no podrá realizar nuevas modificaciones al motivo de la solicitud.",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Indicar revisión",
        })
        .then((result) => {
          if (result.isConfirmed) {
            let solicitud = {
              id_estudiante: this.apelacion[0].id_estudiante.id,
              id_evaluacion: this.apelacion[0].id_evaluacion.id,
              motivo: this.apelacion[0].motivo,
              fecha_creacion: this.apelacion[0].fecha_creacion,
              respuesta: this.apelacion[0].respuesta,
              fecha_respuesta: this.apelacion[0].fecha_respuesta,
              estado: "E",
              id_docente: this.apelacion[0].id_docente,
            };
            let idSolicitud = this.apelacion[0].id;

            axios
              .put(
                `http://localhost:8000/actualizar/solicitud/${idSolicitud}`,
                solicitud
              )
              .then(function (response) {
                that.$swal.fire(
                  "Solicitud actualizada",
                  "La solicitud se encuentra actualmente en revisión",
                  "success"
                ).then((result) => {
                  location.reload();
                });
              });
          }
        });
    },
  },
  created() {
    const that = this;
    let idEstudianteURL = this.idEstudiante;
    let idEvaluacionURL = this.idEvaluacion;
    axios
      .get(
        `http://localhost:8000/solicitudRespuesta/${idEstudianteURL}/${idEvaluacionURL}`
      )
      .then(function (response) {
        that.apelacion = response.data;
      });

    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        that.idDocente = response.data.id;
      });
  },
};
</script>

<style></style>
