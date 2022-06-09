<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSectionV2">
        <h3 class="textTitleV2">Apelaciones</h3>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th style="width: 20%">Curso</th>
            <th style="width: 10%;">Evaluación</th>
            <th style="width: 10%;">Estado</th>
            <th style="width: 30%;">Detalle Motivo</th>
            <th style="width: 25%;">Respuesta</th>
            <th style="width: 5%;"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="solicitud in solicitudes" :key="solicitud.id">
            <Solicitudes :solicitud="solicitud" />
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import Solicitudes from "../../components/Solicitud.vue";
import axios from "axios";

export default {
  data() {
    return {
      solicitudes: [],
    };
  },
  components: {
    Sidebar,
    Navbar,
    Solicitudes,
  },
  mounted() {
    let ins = this;
    let idUsuarioLogeado = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/solicitudes/${idUsuarioLogeado}`)
      .then(function (response) {
        ins.solicitudes = response.data;
      });
  },
};
</script>

<style></style>
