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
        <h4 class="textTitle">Apelaciones</h4>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Nombre Evaluacion</th>
              <th>Estado</th>
              <th>Fecha Creacion</th>
              <th>Estudiante</th>
              <th>Seccion</th>
              <th>Docente</th>
              <th>Detalle</th>
            </tr>
          </thead>
          <tbody v-for="solicitud in solicitudes" :key="solicitud.id">
            <ApelacionesAsignaJefe :solicitud="solicitud"/>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarAutoridad.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import ApelacionesAsignaJefe from '../../components/ApelacionesAsignaJefe.vue';


export default {
  components: {
    Sidebar,
    Navbar,
    ApelacionesAsignaJefe
},
props:['idAsignatura'],
  data(){
      return{
          solicitudes: []
      }
  },
  created() {
    let ins = this;
    let IDasignatura  = this.idAsignatura;
    axios.get(`http://localhost:8000/jefe/asignatura/solicitudes/${IDasignatura}`).then(function (response) {
      console.log(response.data);
      ins.solicitudes = response.data;
    });
  },
 
};
</script>

<style></style>
