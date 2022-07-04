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
        <h3 class="textTitleV2">Evaluaciones</h3>
        <button style="margin-left:750px" type="button" class="botonTabla" @click.prevent="cambioNotas(this.identificacionAsignatura)">
                    Ver cambio de notas
        </button>
        <button style="margin-left:30px" type="button" class="botonTabla" @click.prevent="cambioPonderaciones(this.identificacionAsignatura)">
                    Ver cambio de ponderaciones
        </button>
        <button style="margin-left:30px" type="button" class="botonTabla" @click.prevent="cambioFechas(this.identificacionAsignatura)">
                    Ver cambio de fechas
        </button>
        </div>
      

      <table class="tableV2">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Fecha realizacion</th>
              <th>Fecha limite entrega de notas</th>
              <th>Ponderacion</th>
              <th>Estado</th>
              <th>Observacion</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="evaluacion in evaluaciones" :key="evaluacion.id">
                <td>{{evaluacion.nombre}}</td>
                <!--V-for para obtener todas las tuplas con los distintos profesores-->
                <td> {{evaluacion.fechaEvActual }} </td>
                <td>{{evaluacion.fechaEntrega}}</td>
                <td>{{ parseFloat(evaluacion.ponderacion * 100).toFixed(1) }}% </td>    
                <td v-if="evaluacion.estado == 'P' "> Pendiente </td>
                <td v-else > Evaluada </td>                       
                <td> {{evaluacion.observacion}} </td>
            </tr>
          </tbody>
        </table>
        
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
  props:["idSeccion","idAsignatura"],
  data(){
      return{
          evaluaciones: [],
          identificacionAsignatura: 0,
      }
  },
  created() {
    // Forma de capturar el id del Jefe de Carrera, dado el id del usuario que inició sesión.
    let ins = this;
    let identificacionSeccion = this.idSeccion
    this.identificacionAsignatura = this.idAsignatura
    axios
    .get(`http://localhost:8000/evaluaciones/${identificacionSeccion}`)
    .then(function (response) {
      ins.evaluaciones = response.data;
    });
  },
  mounted(){
    
  },
  methods:{
    cambioNotas(idAsignatura){
      router.push(`/jefe/asignaturas/cambios/nota/${idAsignatura}`)
    },
    cambioFechas(idAsignatura){
        router.push(`/jefe/asignaturas/cambios/fecha/${idAsignatura}`);
    },
    cambioPonderaciones(idAsignatura){
        router.push(`/jefe/asignaturas/cambios/ponderacion/${idAsignatura}`);
    }

  }
};
</script>

<style></style>
