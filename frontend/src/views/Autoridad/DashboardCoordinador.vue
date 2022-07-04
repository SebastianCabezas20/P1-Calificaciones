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
          <p>Totales (pendientes - aprobadas - rechazadas)</p>
          <h3>{{ nSolicitudesT }} ({{nSolicitudesP}} - {{ nSolicitudesA }} - {{ nSolicitudesR }})</h3>
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

