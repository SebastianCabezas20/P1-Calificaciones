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
        <h3 class="textTitleV2">Solicitud de apelación</h3>
      </div>

      <div class="formApelacion" v-for="data in dataSolicitud" :key="data.id">
        <p class="textoFormulario">
          <b>Código:</b> 
          {{ data.id_evaluacion.id_coordinacion.id_asignatura.codigo }}-{{data.id_evaluacion.id_coordinacion.coordinacion}}-{{data.id_evaluacion.id_coordinacion.seccion}}
        </p>
        <p class="textoFormulario">
          <b>Asignatura:</b>
          {{ data.id_evaluacion.id_coordinacion.id_asignatura.nombre }}
        </p>
        <p class="textoFormulario">
          <b>Evaluación:</b> {{ data.id_evaluacion.nombre }}
        </p>
        <p class="textoFormulario"><b>Calificación:</b> {{ data.nota }}</p>
        <p class="textoFormulario">
          <b>Docente evaluador(a):</b> {{ data.id_evaluacion.id_docente.id_usuario.first_name }} {{data.id_evaluacion.id_docente.id_usuario.last_name}}</p>

        <div id="divMotivo">
          <label class="textoFormulario"><b>Motivo</b></label>
          <textarea
            class="cuadroTexto"
            rows="10"
            placeholder="Escriba acá el motivo de su solicitud de apelación"
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
        anterior_nota:null,
        actual_nota:this.dataSolicitud[0].nota,
        fecha_creacion: fechaActual,
        archivoAdjunto: null,
        respuesta: "",
        fecha_respuesta: null,
        estado: "P",
        id_estudiante: this.idEstudiante,
        id_docente: this.dataSolicitud[0].id_evaluacion.id_docente.id,
        id_evaluacion: this.dataSolicitud[0].id_evaluacion.id,
        id_calificacion:this.dataSolicitud[0].id
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
