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

      <!-- Botón que abre el modal para agregar una evaluación. -->
      <button @click="showModal = true" type="button" class="btn btn-primary">
        Agregar Evaluación
      </button>

      <!-- Modal -->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModal">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">
                  Crear Evaluación
                </h5>
                <button
                  type="button"
                  class="btn-close"
                  @click="showModal = false"
                ></button>
              </div>

              <div class="modal-body">
                <form
                  action="#"
                  method="POST"
                  v-on:submit.prevent="crearEvaluacion"
                >
                  <div class="mb-3">
                    <label class="form-label">Nombre de la evaluación</label>
                    <input
                      v-model="nombreEvaluacion"
                      class="form-control"
                      placeholder="PEP 1"
                      required
                    />
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Tipo de Evaluación</label>
                    <select class="form-select" v-model="tipoEvaluacion" required>
                      <option selected disabled> Seleccione un tipo de evaluación </option>
                      <option v-for="tipo in tiposEvaluaciones" v-bind:value="tipo.id">
                        {{ tipo.nombre }}
                      </option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Porcentaje de ponderación</label>
                    <input
                      v-model="porcentajeEvaluacion"
                      class="form-control"
                      placeholder="50"
                      required
                    />
                  </div>
                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      v-on:click="showModal = false"
                    >
                      Cancelar
                    </button>
                    <button type="submit" class="btn btn-primary">
                      Guardar Cambios
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </transition>
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
      tiposEvaluaciones: [],
      showModal: false,
      nombreEvaluacion: "",
      tipoEvaluacion: "",
      porcentajeEvaluacion: "",
    };
  },

  mounted() {
    let that = this;
    axios
      .get("http://localhost:8000/coordinacion/evaluaciones")
      .then(function (response) {
        that.evaluacionesCurso = response.data;
      });

    axios
      .get("http://localhost:8000/evaluacion/tipos")
      .then(function (response) {
        that.tiposEvaluaciones = response.data;
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
          // Funcionando pero quizas falta agregar una alerta emergente que diga que se elimino.
          location.reload();
        });
    },
    crearEvaluacion: function (event) {
      
      // Funcionando. Ahora falta tirar los datos al back y estamos.
      console.log(this.nombreEvaluacion);
      console.log(this.tipoEvaluacion);
      console.log(this.porcentajeEvaluacion);
    },
  },
};
</script>

<style></style>
