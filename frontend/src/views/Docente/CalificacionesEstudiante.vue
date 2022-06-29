<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <!-- Se desea mostrar las evaluaciones y calificaciones de Teoria. -->
      <template v-if="componente === 'T'">
        <Componente
          :componente="this.teoria"
          :evaluaciones="this.evaluaciones"
          :calificaciones="this.calificaciones"
        />
      </template>

      <!-- Se desea mostrar las evaluaciones y calificaciones de Laboratorio. -->
      <template v-else>
        <Componente
          :componente="this.laboratorio"
          :evaluaciones="this.evaluaciones"
          :calificaciones="this.calificaciones"
        />
      </template>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import Componente from "../../components/ComponenteEstudiante.vue";
import axios from "axios";
import router from "../../router";

export default {
  props: ["componente", "codigoAsig", "idUsuario"],
  components: {
    Sidebar,
    Navbar,
    Componente,
  },
  data() {
    return {
      evaluaciones: [],
      calificaciones: [],
      laboratorio: "Laboratorio",
      teoria: "Teoria",
    };
  },

  mounted() {
    let that = this;

    /* Se mostrarán las calificaciones y evaluaciones del estudiante que tiene
    en Teoria. */
    if (this.componente === "T") {
      axios
        .get(
          `http://localhost:8000/calificacionesTeoria/${this.codigoAsig}/${this.idUsuario}`
        )
        .then(function (response) {
          that.calificaciones = response.data[0];
          that.evaluaciones = response.data[1];
        });
    } 
    
    /* Se mostrarán las calificaciones y evaluaciones del estudiante que tiene
    en Laboratorio. */
    else {
      axios
        .get(
          `http://localhost:8000/calificacionesLaboratorio/${this.codigoAsig}/${this.idUsuario}`
        )
        .then(function (response) {
          that.calificaciones = response.data[0];
          that.evaluaciones = response.data[1];
        });
    }
  },
};
</script>

<style></style>
