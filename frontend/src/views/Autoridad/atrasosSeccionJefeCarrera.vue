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
            <h2>Secciones que se han atrasado en entrega de evaluaciones</h2>
            <table class="tableDashboard">
              <thead>
                <tr>
                <th>Coordinacion - Sección</th>
                <th>Componente</th>
                <th>Cantidad de Atrasos</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(seccion_atrasada, indice) in secciones_atrasadas" :key="seccion_atrasada.id">
                <td class="text-center">{{seccion_atrasada.coordinacion}}-{{seccion_atrasada.seccion}}</td>
                <td class="text-center">{{seccion_atrasada.id_asignatura.componente}}</td>
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
    props:['idAsignatura'],
    data(){
        return{
            secciones_atrasadas: [],
            numero_Atrasos: [],
        }
    },
    created() {},
    mounted() {
      let ins = this;
      let idAsignaturaURL = this.idAsignatura
      axios
      .get(`http://localhost:8000/get/seccionesAsignaturaAtrasadas/${idAsignaturaURL}`)
      .then(function (response) {
        ins.secciones_atrasadas = response.data[0];
        ins.numero_Atrasos = response.data[1];
      });
    }
  };
  </script>
  
  <style></style>
  