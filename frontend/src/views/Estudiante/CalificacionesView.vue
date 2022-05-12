<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      
       <div id="filaInformacion" class="row row-cols-3">
            <div class="col" >{{informacionTeoria[0].id_coordinacion.id_asignatura.nombre}}</div>
            <div class="col">nivel:   {{informacionTeoria[0].id_coordinacion.id_asignatura.nivel}}</div>
            <div class="col"> Docente:  {{informacionTeoria[0].id_docente.id_usuario.username}}</div>
        </div> 
  

      <div class="componentCourse">
        <div class="titleSection">
          <h3 class="textTitle">Calificaciones Catedra</h3>
        </div>

        <div class="tableContent">
          <table class="table">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Observacion</th>
                <th>Calificacion</th>
                <th>Ponderacion</th>
                <th>Estado</th>
                <th>Fecha</th>
                <th>Apelar</th>
                <!--Saque estado de la evaluacion-->
              </tr>
            </thead>
            <tbody>
              <tr v-for="calificacion in calificacionesTeoria" :key="calificacion.id">
                <CalificacionInfo :calificacion="calificacion" 
                @EventBoton="(id)=> ingresar(id)"/>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="stateStudent">
          <h4>Estado del estudiante</h4>
        </div>
      </div>

      <div v-if="this.mostrar" id="filaInformacion" class="row row-cols-3">
            <div class="col" >{{informacionLaboratorio[0].id_coordinacion.id_asignatura.nombre}}</div>
            <div class="col">nivel:   {{informacionLaboratorio[0].id_coordinacion.id_asignatura.nivel}}</div>
            <div class="col"> Docente:  {{informacionLaboratorio[0].id_docente.id_usuario.username}}</div>
        </div> 
      <div v-if="this.mostrar" class="componentCourse">
        <div class="titleSection">
          <h3 class="textTitle">Calificaciones laboratorio</h3>
        </div>

        <div class="tableContent">
          <table class="table">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Observacion</th>
                <th>Calificacion</th>
                <th>Ponderacion</th>
                <th>Estado</th>
                <th>Fecha</th>
                <th>Apelar</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="calificacion in calificacionesLaboratorio" :key="calificacion.id">
                <CalificacionInfo :calificacion="calificacion" />
              </tr>
            </tbody>
          </table>
        </div>

        <div class="stateStudent">
          <h4>Estado del estudiante</h4>
        </div>
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
import router from '../../router';

export default {
  data() {
    return {
      calificacionesTeoria: [],
      calificacionesLaboratorio: [],
      informacionTeoria:[],
      informacionLaboratorio:[],
      mostrar: false,
    };
  },
  props:['codigoAsignatura'],
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
  created() {
    let ins = this;
    let codigoAsig = this.codigoAsignatura;
    axios.get(`http://localhost:8000/calificacionesTeoria/${codigoAsig}`).then(function (response) {

      ins.calificacionesTeoria = response.data;
    });
    axios.get(`http://localhost:8000/calificacionesLaboratorio/${codigoAsig}`).then(function (response) {
      if(response.data.length != 0){
        ins.calificacionesLaboratorio = response.data;
        ins.mostrar = true
      }
      
    });
    axios.get(`http://localhost:8000/InformacionTeoria/${codigoAsig}`).then(function (response) {
      console.log(response.data);
      ins.informacionTeoria = response.data;
    });
    axios.get(`http://localhost:8000/InformacionLaboratorio/${codigoAsig}`).then(function (response) {
      if(response.data.length != 0){
        ins.informacionLaboratorio = response.data;
        ins.mostrar = true
      }
    });
    
  },
  methods:{
    ingresar(idCalificacion){
      router.push(`/estudiante/add/solicitud/${idCalificacion}`);
    }
  }
};
</script>

<style>
.componentCourse {
  margin-bottom: 30px;
}

.stateStudent {
  background-color: #eeeeee;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  padding: 10px;
}
</style>
