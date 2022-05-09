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
            <tr v-for="(evaluacion, index) in evaluacionesCurso" :key="index">
              <td>{{ evaluacion.nombre }}</td>
              <td>{{ evaluacion.id_tipoEvaluacion.nombre }}</td>
              <td>{{ evaluacion.fechaEvActual }}</td>
              <td>{{ evaluacion.estado }}</td>
              <td>{{ evaluacion.ponderacion }}</td>
              <td>
                <div class="text-center">
                  <i class="fa-solid fa-pencil"></i>
                </div>
              </td>
              <td>
                <div class="text-center">
                  <button
                    class="fa-solid fa-trash-can"
                    v-on:click="deleteEvaluacion($event, index)"
                  ></button>
                </div>
              </td>
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
import axios from "axios";

export default {
  components: {
    Sidebar,
    Navbar,
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

  methods: {
    deleteEvaluacion: function (event, index) {
      let idEvaluacionEliminar = this.evaluacionesCurso[index].id;
      axios
        .delete(
          `http://localhost:8000/delete/evaluacion/${idEvaluacionEliminar}`
        )
        .then(function (response) {
          location.reload();
          // Funcionando pero quizas falta agregar una alerta emergente que diga que se elimino.
        });
    },
  },
};
</script>

<style></style>
