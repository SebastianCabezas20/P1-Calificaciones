<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSection">
        <h3 class="textTitle">Solicitud de Apelación</h3>
      </div>

      <div class="formApelacion" v-for="data in dataSolicitud">
        <h5 class="textoFormulario">
          Nombre Evaluacion: {{ data.id_evaluacion.nombre }}
        </h5>
        <h5 class="textoFormulario">
          Nombre Asignatura:
          {{ data.id_evaluacion.id_coordinacion.id_asignatura.nombre }}
        </h5>
        <h5 class="textoFormulario">Nota: {{ data.nota }}</h5>

        <div id="divMotivo">
          <h5 class="textoFormulario">Motivo de la solicitud</h5>
          <textarea
            placeholder="Escriba acá su solicitud"
            id="motivoSolicitud"
            v-model="motivoSolicitud"
          ></textarea>
        </div>

        <button v-on:click="submitApelacion" class="buttonForm">Apelar</button>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";
import axios from "axios";
import router from "../../router";

export default {
  props: ["idCalificacion"],

  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
  data() {
    return {
      dataSolicitud: [],
      idEstudiante: 0,
      motivoSolicitud: "",
    };
  },
  mounted() {
    const that = this;
    let identificacionUsuario = this.$store.getters.idUsuario;
    let IdentificacionCalificacion = this.idCalificacion;

    axios
      .get(`http://localhost:8000/api/estudiante/${identificacionUsuario}`)
      .then(function (response) {
        that.idEstudiante = response.data.id;
      });

    axios
      .get(
        `http://localhost:8000/informacion/solicitud/estudiante/${IdentificacionCalificacion}`
      )
      .then(function (response) {
        that.dataSolicitud = response.data;
      });
  },
  methods: {
    submitApelacion() {
      const that = this;
      let fechaActual = new Date();
      fechaActual = fechaActual.toISOString().slice(0, 10);

      let solicitudFinal = {
        motivo: this.motivoSolicitud,
        fecha_creacion: fechaActual,
        archivoAdjunto: null,
        respuesta: "",
        fecha_respuesta: null,
        estado: "P",
        id_estudiante: this.idEstudiante,
        id_docente: this.dataSolicitud[0].id_evaluacion.id_docente.id,
        id_evaluacion: this.dataSolicitud[0].id_evaluacion.id,
      };

      axios
        .post("http://localhost:8000/add/solicitud", solicitudFinal)
        .then(function (response) {
          router.push(
            `/estudiante/calificaciones/${that.dataSolicitud[0].id_evaluacion.id_coordinacion.id_asignatura.codigo}`
          );
        });
    },
  },
};
</script>

<style></style>
