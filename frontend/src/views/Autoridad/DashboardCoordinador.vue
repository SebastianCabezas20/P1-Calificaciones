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
        <!-- Cuadro con las coordinaciones inscritas por el coordinador. -->
        <div
          class="col cuadradoDashboard"
          style="margin-right: 20px"
          @click="coordinaciones()"
        >
          <div class="iconoDashboard">
            <span class="fa-solid fa-book fa-3x"></span>
          </div>
          <h2>Coordinaciones a cargo este semestre</h2>
          <p>Totales</p>
          <h3>
            {{ Number(nCursos) }}
          </h3>
        </div>

        <!-- Cuadro con solicitudes totales, pendientes y recibidas. -->
        <div
          class="col cuadradoDashboard"
          style="margin-left: 20px"
          @click="solicitudes()"
        >
          <div class="iconoDashboard">
            <span class="fa-solid fa-file-circle-exclamation fa-3x"></span>
          </div>
          <h2>Solicitudes de revisión recibidas en mis coordinaciones</h2>
          <p>Totales (pendientes - aprobadas - rechazadas - En revision)</p>
          <h3>{{ nSolicitudesT }} ({{nSolicitudesP}} - {{ nSolicitudesA }} - {{ nSolicitudesR }}-{{ nSolicitudesE }})</h3>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col">
            <div class="row">
              <div style=" width: 50%; float: left; ">
                <h3>Atrasos en la entrega de calificaciones</h3>
                  <div class="chart-container" style="position: relative; height:350px; width:350px">
                    <canvas id="graficoPie-atrasos" style=""></canvas>
                  </div>
              </div>
              <div style=" width: 50%; float: left; ">
                <h3>Cambio de calificaciones</h3>
                  <div class="chart-container" style="position: relative; height:350px; width:350px">
                    <canvas id="graficoPie-notas" style=""></canvas>
                  </div>
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
import { Chart } from "chart.js";


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
      nEvaluacionesP: 0,
      nSolicitudesT: 0,
      nSolicitudesP: 0,
      nSolicitudesA: 0,
      nSolicitudesR: 0,
      nSolicitudesE: 0,
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
        ins.cambio_notas = response.data;
      });

    axios
      .get(`http://localhost:8000/get/infodashboardcoordinador/${identificacionUsuario}`)
      .then(function (response) {
        ins.nCursos = response.data[0];
        ins.nEvaluacionesP = response.data[1];
        ins.nSolicitudesT = response.data[2];
        ins.nSolicitudesP = response.data[3];
        ins.nSolicitudesA = response.data[4];
        ins.nSolicitudesR = response.data[5];
        ins.nSolicitudesE = response.data[6];
      });



     // Grafico para atrasos
    axios
    .get(`http://localhost:8000/get/dash/atrasos/coordinador/${identificacionUsuario}`)
    .then(function (response){
      console.log(response.data[1])  
      const ctx3 = document.getElementById('graficoPie-atrasos').getContext('2d');
    const graficoPieFechas = new Chart(ctx3, {
      type: 'doughnut',
      data: {
        labels: response.data[1],
        datasets: [{
          label: '# cambio fecha',
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

    // Grafico para cambio notas
    axios
    .get(`http://localhost:8000/get/dash/cambioNotas/coordinador/${identificacionUsuario}`)
    .then(function (response){
      console.log(response.data[1])  
      const ctx4 = document.getElementById('graficoPie-notas').getContext('2d');
    const graficoPieFechas = new Chart(ctx4, {
      type: 'doughnut',
      data: {
        labels: response.data[1],
        datasets: [{
          label: '# cambio fecha',
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
    solicitudes(){
      this.$router.push({ name: "seccionesCoordinador" });
    },

    coordinaciones() {
      this.$router.push({ name: "asignaturasCoordinador" });
    }
  },
};
</script>

<style>
</style>

