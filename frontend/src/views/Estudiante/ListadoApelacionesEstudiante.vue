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
              <th>Título</th>
              <th>Curso</th>
              <th>Evaluación</th>
              <th>Estado</th>
              <th>Detalle Motivo</th>
              <th>Respuesta</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="solicitud in solicitudes" :key="solicitud.id">
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
  },
  mounted() {
    let ins = this;
    axios.get("http://localhost:8000/solicitudes").then(function (response) {
      console.log(response.data);
      ins.solicitudes = response.data;
    });
  },
};
</script>

<style></style>
