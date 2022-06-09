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
          <h1>Información dashboard</h1>
        </div>

        <div class="row">
          <div class="col">
            Cursos Totales:
          </div>
          <div class="col">
            Evaluaciones Pendientes:
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes totales:
          </div>
          <div class="col">
            Solicitudes Pendientes:
          </div>
        </div>
        <div class="row">
          <div class="col">
            Aprobadas:
          </div>
          <div class="col">
            Rechazadas:
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <h1>Cambios en Calificaciones</h1>
        </div>
        <div class="row">
          <div class="col">

            <div class="tableContent">
              <table class="tableV2">
                <thead>
                  <tr>
                    <th>Nombre Evaluación</th>
                    <th>Nombre Asignatura</th>
                    <th>Nombre Alumno</th>
                    <th>Nombre profesor</th>
                    <th>Fecha cambio</th>
                    <th>Nota Anterior</th>
                    <th>Nota Nueva</th>
                    <th>Motivo</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="cambio_nota in cambio_notas" :key="cambio_nota.id">
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.nombre }}</td>
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_estudiante.id_usuario.first_name }}
                      {{ cambio_nota.id_calificacion.id_estudiante.id_usuario.last_name }}</td>
                      <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.id_docente.id_usuario.first_name }}
                      {{ cambio_nota.id_calificacion.id_evaluacion.id_docente.id_usuario.last_name }}</td>
                    <td class="text-center">{{ cambio_nota.fecha_cambio }}</td>
                    <td class="text-center">{{ cambio_nota.anterior_nota }}</td>
                    <td class="text-center">{{ cambio_nota.actual_nota }}</td>
                    <td class="text-center">{{ cambio_nota.motivo }}</td>
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
      cambio_notas:[],
    }
  },
  created() {
    let ins = this;
    axios
      .get(`http://localhost:8000/get/cambiosNota`)
      .then(function (response) {
        console.log(response.data);
        ins.cambio_notas = response.data;
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
  methods: {  }
};
</script>

<style>
</style>

