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
        <div class="col-md-3" id="solPendientes" @click="solicitudes()">
          <!-- Icono -->
          <div class="iconoDashboard">
            <span class="fa-solid fa-file-circle-exclamation fa-3x"></span>
          </div>
          <!-- Texto -->
          <h2>Solicitudes de revisión pendientes</h2>
          <!-- Dato -->
          <h3>{{ solicitudesPendientes }} - {{ solicitudesTotales }}</h3>
        </div>
        <div class="col-md"></div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      solicitudesPendientes: 0,
      solicitudesTotales: 0,
    };
  },
  mounted() {
    let identificacionUsuario = this.$store.getters.idUsuario;
    let that = this;
    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        let idDocente = response.data.id;
        axios
          .get(`http://localhost:8000/solicitudesDocente/${idDocente}`)
          .then(function (responseTwo) {
            let solicitudes = responseTwo.data;
            // Obtención núm. de solicitudes totales.
            that.solicitudesTotales = solicitudes.length;

            // Obtención núm. de solicitudes pendientes.
            for (var i = 0; i < solicitudes.length; i++) {
              if (solicitudes[i].estado == "P") {
                that.solicitudesPendientes++;
              }
            }
          });
      });
  },
  methods: {
    solicitudes() {
      this.$router.push({ name: "Apelacionesdocente" });
    },
  },
};
</script>

<style></style>
