<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">

      <div class="container">
        <div class="row">
          <h1>Inicio</h1>
        </div>

        <div class="row">
          <div class="col">
            Estudiantes en Carrera: {{ Number(nEstudiantes) }}
          </div>
          <div class="col">
            Solicitudes realizadas en semestre: {{ Number(nSolicitudesS) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes Pendientes: {{ Number(nSolicitudesP) }}
          </div>
          <div class="col">
            Solicitudes aprobadas: {{ Number(nSolicitudesA) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes rechazadas: {{ Number(nSolicitudesR) }}
          </div>
          <div class="col">
            Notas cambiadas: {{ Number(nNotasCambiadas) }}
          </div>
        </div>
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
  data() {
    return {
      nEstudiantes: [],
      nSolicitudesS: [],
      nSolicitudesP: [],
      nSolicitudesA: [],
      nSolicitudesR: [],
      nNotasCambiadas: [],
      etiquetas:[],
      dataRechazados:[],
      dataPendientes:[],
      dataAceptados:[],
    }
  },
  created() {
    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;

    axios
      .get(`http://localhost:8000/get/infodashboardjefecarrera/${identificacionUsuario}`)
      .then(function (response) {
        console.log(response.data);
        ins.nEstudiantes = response.data[0];
        ins.nSolicitudesS = response.data[1];
        ins.nSolicitudesP = response.data[2];
        ins.nSolicitudesA = response.data[3];
        ins.nSolicitudesR = response.data[4];
        ins.nNotasCambiadas = response.data[5];
      });
    
      },
    mounted(){
      let ins = this;
      let identificacionUsuario = this.$store.getters.idUsuario;
    axios
    .get(`http://localhost:8000/get/dash/solicitudes/${identificacionUsuario}`)
    .then(function (response) {      
      //////////////////////////////////////////////////
      const ctx = document.getElementById('graficoBarras').getContext('2d');
      const graficoBarras = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: response.data[0],
          datasets: [{
            label: 'Rechazadas',
            data: response.data[1],
            backgroundColor: [
              'rgba(255, 99, 132)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 0
          },
          {
            label: 'Aceptadas',
            data: response.data[3],
            backgroundColor: [
              'rgba(54, 162, 235)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 0
          },
          {
            label: 'Pendientes',
            data: response.data[2],
            backgroundColor: [
              'rgba(255, 206, 86)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 0
          },
          ],

        },
        options: {
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            }
          }
        }
      });


    });
    
    axios
    .get(`http://localhost:8000/get/dash/cambioNotas/${identificacionUsuario}`)
    .then(function (response){  
      const ctx2 = document.getElementById('graficoPie').getContext('2d');
    const graficoPie = new Chart(ctx2, {
      type: 'pie',
      data: {
        labels: response.data[1],
        datasets: [{
          label: '# cambio notas',
          data: response.data[0],
          backgroundColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 0
        }]
      },
      options: {
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
          }
        }
      }
    });

    });
    
    
    
  },
  methods: {

  }
};
</script>

<style>
</style>
