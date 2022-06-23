<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
    <div class="row" style="background-color: #ffffff">
        <div class="col-md--fluid rectanguloDashboard">
          <h2>Asignaturas que se han atrasado en entrega de evaluaciones</h2>
          <table class="tableDashboard">
            <thead>
              <tr>
              <th>Código</th>
              <th>Nombre Asignatura</th>
              <th>Componente</th>
              <th>Cantidad de Atrasos</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(asignatura_atrasada, indice) in asignaturas_atrasadas" :key="asignatura_atrasada.id">
              <td class="text-center">{{asignatura_atrasada.codigo}}</td>
              <td class="text-center">{{asignatura_atrasada.nombre}}</td>
              <td class="text-center">{{asignatura_atrasada.componente}}</td>
              <td class="text-center">{{numero_Atrasos[indice]}}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col-md-3"></div>
      </div>
      
    </div>
    
  </div>
  

</template>

<script>
import Sidebar from "../../components/SidebarJefeCarrera.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import router from "../../router";


export default {
  components: {
    Sidebar,
    Navbar,
  },
  data(){
      return{
          asignaturas_atrasadas: [],
          numero_Atrasos: [],
      }
  },
  created() {},
  mounted() {
    let ins = this;
    axios
    .get(`http://localhost:8000/get/asignaturasAtrasadas`)
    .then(function (response) {
      console.log(response.data);
      ins.asignaturas_atrasadas = response.data[0];
      ins.numero_Atrasos = response.data[1];
    });


  }
};
</script>

<style></style>
