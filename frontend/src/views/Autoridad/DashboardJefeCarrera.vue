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
          <h2>Asignaturas con atrasos en evaluaciones</h2>
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

    const ctx = document.getElementById('graficoBarras').getContext('2d');
    const graficoBarras = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Asignatura 1', 'Asignatura 2', 'Asignatura 3', 'Asignatura 4', 'Asignatura 5', 'Asignatura 6'],
        datasets: [{
            label: 'Rechazadas',
            data: [12, 19, 3, 5, 2, 3],
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
            borderWidth: 3
        },
        {
            label: 'Aceptadas',
            data: [1, 1, 31, 51, 21, 31],
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
            borderWidth: 3
        },
        {
            label: 'Pendientes',
            data: [1, 1, 31, 51, 21, 31],
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
            borderWidth: 3
        },
        ],
        
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
        labels: ['Asignatura 1', 'Asignatura 2', 'Asignatura 3', 'Asignatura 4', 'Asignatura 5', 'Asignatura 6'],
        datasets: [{
            label: '# de coordinaciones',
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
