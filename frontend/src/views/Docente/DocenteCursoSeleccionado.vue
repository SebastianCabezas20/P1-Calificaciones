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
        <h3 class="textTitle">Docencia: Evaluaciones del curso X</h3>
      </div>

      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Evaluación</th>
              <th>Tipo</th>
              <th>Fecha de Rendición</th>
              <th>Estado</th>
              <th>Ponderación</th>
              <th>Icono de Calificar</th>
              <th>Icono de Eliminar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="evaluacion in evaluacionesCurso" :key="evaluacion.id">
              <EvaluacionesCurso :evaluacionCurso="evaluacion" />
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import EvaluacionesCurso from "../../components/EvaluacionesCurso.vue";
import axios from 'axios'

export default {
  components: {
    Sidebar,
    Navbar,
    EvaluacionesCurso,
  },
  data() {
    return {
      evaluacionesCurso: [],
    };
  },

  mounted() {
    let that = this;
    axios
      .get("http://localhost:8000/coordinacion/evaluaciones")
      .then(function (response) {
        that.evaluacionesCurso = response.data;
      });
  },
};
</script>

<style></style>
