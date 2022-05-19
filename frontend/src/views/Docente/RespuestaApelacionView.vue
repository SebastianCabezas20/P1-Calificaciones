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
          <h6 class="textoFormulario">Calificación: {{ notaJson[0].nota }}</h6>

          <form class="mt-2">
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
                placeholder="Nueva calificación"
              />
            </div>

            <button class="submitButton" @click.prevent="send">
              Enviar Respuesta
            </button>
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
      notaJson: [],
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
      if (this.respuestaActual == "" || this.isAceptar == null) {
        alert("Se necesita añadir una respuesta");
      } else if (
        (this.isAceptar == true && this.notaActual <= 0) ||
        this.notaActual > 7
      ) {
        alert("Nota debe ser de 1 a 7");
      } else {
        let idEstudianteSolicitud = this.idEstudiante;
        let idEvaluacionSolicitud = this.idEvaluacion;
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
              id_estudiante: this.notaJson[0].id_estudiante,
              id_evaluacion: this.notaJson[0].id_evaluacion,
              id_observacion: this.notaJson[0].id_observacion,
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
        that.apelacion = response.data[0];
        that.notaJson = response.data[1];
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
