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
            Cursos Actuales: {{ Number(nCursos) }}
          </div>
          <div class="col">
            Evaluaciones Realizadas: {{ Number(nEvaluacionesR) }}
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
          <h1>Próximas evaluaciones</h1>
        </div>
        <div class="row">
          <div class="col">
            Evaluaciones
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <h1>Próximas calificaciones</h1>
        </div>
        <div class="row">
          <div class="col">

            <table class="tableV2">
              <thead>
                <tr>
                  <th class="row-Nombre">Asignatura</th>
                  <th> Evaluación </th>
                  <th class="row-Horario">Fecha Estimada</th>
                </tr>
              </thead>
            </table>

          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";


export default {
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      nCursos: [],
      nEvaluacionesR: [],
      nSolicitudesT: [],
      nSolicitudesP: [],
      nSolicitudesA: [],
      nSolicitudesR: [],
      mostrar: false,
    };
  },

  mounted() {

    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;

    axios
      .get(`http://localhost:8000/get/infodashboardestudiante/${identificacionUsuario}`)
      .then(function (response) {
        console.log(response.data);
        ins.nCursos = response.data[0];
        ins.nEvaluacionesR = response.data[1];
        ins.nSolicitudesT = response.data[2];
        ins.nSolicitudesP = response.data[3];
        ins.nSolicitudesA = response.data[4];
        ins.nSolicitudesR = response.data[5];
      });

  }

};
</script>

<style>
</style>
