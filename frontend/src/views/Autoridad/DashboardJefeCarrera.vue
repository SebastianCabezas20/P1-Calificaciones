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
        <h4 class="textTitle">Cambios de Fecha</h4>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Nombre Evaluación</th>
              <th>Nombre Asignatura</th>
              <th>Docente</th>
              <th>Fecha del cambio</th>
              <th>Fecha Anterior</th>
              <th>Fecha Nueva</th>
              <th>Motivo</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="cambio_fecha in cambio_fechas" :key="cambio_fecha.id">
              <td class="text-center">{{cambio_fecha.id_evaluacion.nombre}}</td>
              <td class="text-center">{{cambio_fecha.id_evaluacion.id_coordinacion.id_asignatura.nombre}}</td>
              <td class="text-center">{{cambio_fecha.id_evaluacion.id_docente.id_usuario.first_name}} {{cambio_fecha.id_evaluacion.id_docente.id_usuario.last_name}}</td>
              <td class="text-center">{{cambio_fecha.fecha_cambio}}</td>
              <td class="text-center">{{cambio_fecha.fechaAnterior}}</td>
              <td class="text-center">{{cambio_fecha.fechaNueva}}</td>
              <td class="text-center">{{cambio_fecha.motivo}}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="row">
        <div class="chart-container" style="position: relative; height:400px; width:400px">
        <canvas id="graficoBarras"></canvas>
        </div>
        <div class="chart-container" style="position: relative; margin-left:100px; height:400px; width:400px">
        <canvas id="graficoPie" style=""></canvas>
        </div>
      </div>
    </div>
    
  </div>
  

</template>

<script>
import Sidebar from "../../components/SidebarJefeCarrera.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import router from "../../router";
import Chart from 'chart.js/auto';



export default {
  components: {
    Sidebar,
    Navbar,
  },
  data(){
      return{
          cambio_fechas: [],
      }
  },
  created() {
    // Forma de capturar el id del Jefe de Carrera, dado el id del usuario que inició sesión.
    let ins = this;
    axios
    .get(`http://localhost:8000/get/cambiosFecha`)
    .then(function (response) {
      console.log(response.data);
      ins.cambio_fechas = response.data;
    });
  },
  mounted() {
    const ctx = document.getElementById('graficoBarras').getContext('2d');
    const graficoBarras = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 3
        }]
    },
    options: {
        maintainAspectRatio:false,
        scales: {
            y: {
                beginAtZero: true,
            }
        }
    }
    });
    const ctx2 = document.getElementById('graficoPie').getContext('2d');
    const graficoPie = new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 3
        }]
    },
    options: {
        maintainAspectRatio:false,
        scales: {
            y: {
                beginAtZero: true,
            }
        }
    }
    });
    
  },
  methods: {

  }
};
</script>

<style></style>
