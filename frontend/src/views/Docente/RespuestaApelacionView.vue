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
        <div class="formApelacion">
          <h6 class="textoFormulario">
            Asignatura:
            {{
              apelacion[0].id_evaluacion.id_coordinacion.id_asignatura.nombre
            }}
          </h6>
          <h6 class="textoFormulario">
            Evaluación: {{ apelacion[0].id_evaluacion.nombre }}
          </h6>
          <h6 class="textoFormulario">
            Calificación: {{ apelacion[0].id_calificacion.nota }}
          </h6>

          <form class="mt-2" @submit.prevent="send">
            <div class="itemFormulario">
              <label for="nombreUsuarioEstudiante">Estudiante</label>
              <input
                class="form-control relative block w-full"
                id="nombreUsuarioEstudiante"
                type="text"
                :value="apelacion[0].id_estudiante.id_usuario.username"
                disabled
                readonly
              />
            </div>

            <div class="itemFormulario">
              <label for="ApelacionContenido">Motivo de la apelación</label>
              <textarea
                class="form-control relative block w-full"
                id="ApelacionContenido"
                :value="apelacion[0].motivo"
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
                placeholder="Respuesta del Docente"
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

      if (this.isAceptar == true && this.notaActual == null) {
        alert(
          "Para aceptar una solicitud, debe ingresar la nueva nota del estudiante"
        );
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
