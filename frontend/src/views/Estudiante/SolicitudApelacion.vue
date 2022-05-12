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
        .then(function (response) {});
    },
  },
};
</script>

<style>
.formApelacion {
  background: #eeeeee;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  width: 50%;
  overflow-y: auto;
  overflow-x: hidden;
  border-radius: 5px;
  padding: 20px;
}

.textoFormulario {
  display: block;
}

.buttonForm {
  display: block;
  margin-top: 10px;
  background-color: #004883;
  border: 2px solid #fff;
  border-radius: 5px;
  width: 25%;
  text-align: center;
  font-weight: bold;
  padding: 10px 15px;
  color: #fff;
}

#motivoSolicitud {
  display: block;
  width: 95%;
  border: 1px solid #004883;
}

#divMotivo {
  margin-top: 40px;
}
</style>
