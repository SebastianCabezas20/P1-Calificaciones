<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSection">
        <h3 class="textTitle">Mis Apelaciones</h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Curso</th>
              <th>Evaluación</th>
              <th>Estado</th>
              <th>Detalle Motivo</th>
              <th>Respuesta</th>
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
