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
            Cursos Totales: {{ Number(nCursos) }}
          </div>
          <div class="col">
            Evaluaciones Pendientes: {{ Number(nEvaluacionesP) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes totales: {{ Number(nSolicitudesT) }}
          </div>
          <div class="col">
            Solicitudes Pendientes: {{ Number(nSolicitudesP) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Aprobadas: {{ Number(nSolicitudesA) }}
          </div>
          <div class="col">
            Rechazadas: {{ Number(nSolicitudesR) }}
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col">
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
      </div>

    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import router from "../../router";
import Chart from 'chart.js/auto';


export default {
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      cambio_notas: [],
      info: [],
      nCursos: [],
      nEvaluacionesP: [],
      nSolicitudesT: [],
      nSolicitudesP: [],
      nSolicitudesA: [],
      nSolicitudesR: [],
    }
  },
  created() {

  },
  mounted() {

    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/get/cambiosNota/${identificacionUsuario}`)
      .then(function (response) {
        console.log(response.data);
        ins.cambio_notas = response.data;
      });

    axios
      .get(`http://localhost:8000/get/infodashboardcoordinador/${identificacionUsuario}`)
      .then(function (response) {
        console.log(response.data);
        ins.nCursos = response.data[0];
        ins.nEvaluacionesP = response.data[1];
        ins.nSolicitudesT = response.data[2];
        ins.nSolicitudesP = response.data[3];
        ins.nSolicitudesA = response.data[4];
        ins.nSolicitudesR = response.data[5];
      });



    const ctx = document.getElementById('graficoBarras').getContext('2d');
    const graficoBarras = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['curso 1', 'curso 2', 'curso 3', 'curso 4', 'curso 5', 'curso 6'],
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
        maintainAspectRatio: false,
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
        labels: ['Rechazadas', 'Aprobadas'],
        datasets: [{
          label: '# de Solicitudes',
          //Falta buscar una forma de agregar esos datos aca!
          data: [this.nSolicitudesR, this.nSolicitudesA],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)'
          ],
          borderWidth: 3
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

  },
  methods: {}
};
</script>

<style>
</style>

