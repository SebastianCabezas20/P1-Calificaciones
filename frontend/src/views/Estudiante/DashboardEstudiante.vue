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
        
        <!-- Fila 1: Cuadro con las coordinaciones inscritas por el docente. -->
        <div
          class="col cuadradoDashboard"
          style="margin-right: 20px"
          @click="coordinaciones()"
        >
          <div class="iconoDashboard">
            <span class="fa-solid fa-book fa-3x"></span>
          </div>
          <h2>Coordinaciones inscritas este semestre</h2>
          <p>Totales (teoría - laboratorio)</p>
          <h3>
            {{ nCursosTotales }} ({{ nCursosTeoria }} -
            {{ nCursosLaboratorio }})
          </h3>
        </div>

        <!-- Fila 1: Grafico de barras que contiene las solicitudes pendientes, 
          en revisión, aprobadas y rechazadas. -->
        <div class="col cuadradoDashboard d-flex justify-content-between" style="margin-right: 20px" @click="solicitudes()">
          <div>
            <div class="iconoDashboard">
              <span class="fa-solid fa-book fa-3x"></span>
            </div>
            <h2>Solicitudes de revisión realizadas este semestre</h2>
            <p>Totales (pendientes - en revisión - aprobadas - rechazadas)</p>
            <h3>
              {{ nSolicitudesT }} ({{ nSolicitudesP }} - {{ nSolicitudesRevision }} - {{ nSolicitudesA }} - {{ nSolicitudesR }})
            </h3>
          </div>
          <div class="chart-container" style="float: right; width: 250px; margin: auto">
            <canvas id="graficoCircular-Solicitudes"></canvas>
          </div>
        </div>
      </div>

      <!-- Tabla que muestra las tres últimas respuestas de solicitudes 
          de revisión -->
      <div class="row" style="background-color: #ffffff">
        <div class="col rectanguloDashboard">
          <div>
            <h2>Solicitudes de revisión respondidas recientemente</h2>
            <TablaSolicitudes :solicitudes="this.detallesSolicitudes" />
          </div>
        </div>
      </div>

      <!-- Tabla que muestra las tres últimas calificaciones recibidas -->
      <div class="row" style="background-color: #ffffff">
        <div class="col rectanguloDashboard">
          <h2>Calificaciones recibidas recientemente</h2>
          <TablaCalificaciones
            :calificaciones="this.calificacionesEstudiante"
            @EventIngresarCurso="(index) => ingresarCurso(index)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import TablaSolicitudes from "../../components/TablaSolicitudesBasica.vue";
import TablaCalificaciones from "../../components/TablaCalificacionesBasica.vue";
import axios from "axios";
import Chart from "chart.js/auto";

export default {
  components: {
    Sidebar,
    Navbar,
    TablaSolicitudes,
    TablaCalificaciones,
  },
  data() {
    return {
      nCursosTotales: 0,
      nCursosLaboratorio: 0,
      nCursosTeoria: 0,
      detallesSolicitudes: [],
      calificacionesEstudiante: [],

      nSolicitudesT: 0,
      nSolicitudesP: 0,
      nSolicitudesA: 0,
      nSolicitudesR: 0,
      nSolicitudesRevision: 0,
      mostrar: false,
    };
  },

  created() {
    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;

    axios
      .get(
        `http://localhost:8000/get/calificaciones/estudiante/${identificacionUsuario}`
      )
      .then(function (response) {
        ins.calificacionesEstudiante = response.data;
      });

    axios
      .get(
        `http://localhost:8000/get/infodashboardestudiante/${identificacionUsuario}`
      )
      .then(function (response) {
        /* Cálculo de los cursos totales del estudiante. Además de los
        pertenecientes a laboratorio y teoria. */
        ins.nCursosTotales = response.data[0].length;
        for (var i = 0; i < response.data[0].length; i++) {
          if (
            response.data[0][i].id_coordinacion.id_asignatura.componente === "T"
          ) {
            ins.nCursosTeoria++;
          } else {
            ins.nCursosLaboratorio++;
          }
        }

        ins.nSolicitudesRevision = response.data[1];
        ins.nSolicitudesT = response.data[2];
        ins.nSolicitudesP = response.data[3];
        ins.nSolicitudesA = response.data[4];
        ins.nSolicitudesR = response.data[5];
        ins.detallesSolicitudes = response.data[6];

        const ctx2 = document
          .getElementById("graficoCircular-Solicitudes")
          .getContext("2d");
        const graficoPieNotas = new Chart(ctx2, {
          type: "pie",
          data: {
            labels: ["Pendientes", "Aprobadas", "Rechazadas", "En revisión"],
            datasets: [
              {
                label: "Solicitudes del estudiante",
                data: [
                  ins.nSolicitudesP,
                  ins.nSolicitudesA,
                  ins.nSolicitudesR,
                  ins.nSolicitudesRevision,
                ],
                backgroundColor: [
                  "rgb(255, 205, 86)",
                  "#469536",
                  "rgb(255, 99, 132)",
                  "rgb(54, 162, 235, 1)",
                ],
                hoverOffset: 1,
              },
            ],
          },
        });
      });
  },

  methods: {
    ingresarCurso(index) {
      let codigoAsignatura =
        this.calificacionesEstudiante[index].id_evaluacion.id_coordinacion
          .id_asignatura.codigo;
      this.$router.push({
        path: `/estudiante/calificaciones/${codigoAsignatura}`,
      });
    },

    solicitudes() {
      this.$router.push({ name: "ApelacionesEstudiante" });
    }
  },
};
</script>

<style></style>
