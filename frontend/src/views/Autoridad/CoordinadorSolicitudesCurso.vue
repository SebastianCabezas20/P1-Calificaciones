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
              <th>Detalle</th>
            </tr>
          </thead>
          <tbody v-for="solicitud in solicitudes" :key="solicitud.id">
            <ApelacionesCoordinador :solicitud="solicitud" />
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
import ApelacionesCoordinador from "../../components/ApelacionesCoordinador.vue";
import router from "../../router";


export default {
  components: {
    Sidebar,
    Navbar,
    ApelacionesCoordinador
},
props:['idCurso'],
  data(){
      return{
          solicitudes: [],
      }
  },
  created() {
    let ins = this;
    let IDcurso = this.idCurso;
    axios.get(`http://localhost:8000/coordinacion/solicitudes/${IDcurso}`).then(function (response) {
      console.log(response.data);
      ins.solicitudes = response.data;
    });
},
};
</script>

<style></style>
