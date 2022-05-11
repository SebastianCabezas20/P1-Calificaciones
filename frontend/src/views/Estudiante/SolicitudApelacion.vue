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

      <div class="formApelacion">
        <h5 class="textoFormulario">Nombre Evaluacion: {{dataSolicitud[0].id_evaluacion.nombre}}</h5>
        <h5 class="textoFormulario">Nombre Asignatura: {{dataSolicitud[0].id_evaluacion.id_coordinacion.id_asignatura.nombre}}</h5>
        <h5 class="textoFormulario">Nota:  {{dataSolicitud[0].nota}}</h5>
        

        <div id="divMotivo">
          <h5 class="textoFormulario">Motivo de la solicitud</h5>
          <textarea
            placeholder="Escriba acá su solicitud"
            id="motivoSolicitud"
          ></textarea>
        </div>

        <button class="buttonForm">Apelar</button>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";
import axios from 'axios';


export default {
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
  data(){
    return{
      dataSolicitud:[],
      idEstudiante:0,
    }
  },
  props:['idCalificacion'],
  created(){
    const that = this 
    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/api/estudiante/${identificacionUsuario}`)
      .then(function (response) {
        that.idEstudiante = response.data.id;
      });
    let IDcalificacion = this.idCalificacion 
    axios.get(`http://localhost:8000/informacion/solicitud/estudiante/${IDcalificacion}`).then(function (response) {

      that.dataSolicitud = response.data;
    });
  }
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
