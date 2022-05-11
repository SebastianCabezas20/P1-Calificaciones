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
              <th>Modificar Fecha</th>
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
              <td>
                <div class="text-center">
                  <button
                    @click="(showModalFecha = true), (modalIndex = index)"
                    class="fa-solid fa-pencil"
                  ></button>
                </div>
              </td>
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
                    <select
                      class="form-select"
                      v-model="tipoEvaluacion"
                      required
                    >
                      <option selected disabled>
                        Seleccione un tipo de evaluación
                      </option>
                      <option
                        v-for="tipo in tiposEvaluaciones"
                        v-bind:value="tipo.id"
                      >
                        {{ tipo.nombre }}
                      </option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="fechaDeEvaluacion"
                      >Fecha tentativa de evaluación</label
                    >
                    <input
                      v-model="fechaEvActual"
                      id="fechaDeEvaluacion"
                      class="form-control"
                      type="date"
                      required
                    />
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
                    <button
                      @click="showModal = false"
                      type="submit"
                      class="btn btn-primary"
                    >
                      Guardar Cambios
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- Modal Modificar Fecha-->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModalFecha">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">
                  Modificar Fecha Evaluación
                </h5>
                <button
                  type="button"
                  class="btn-close"
                  @click="showModalFecha = false"
                ></button>
              </div>

              <div class="modal-body">
                <form
                  action="#"
                  method="PUT"
                  v-on:submit.prevent="modificarFecha($event, modalIndex)"
                >
                  <div class="mb-3">
                    <label class="form-label"
                      >Nueva Fecha de la Evaluación</label
                    >
                    <input
                      v-model="fechaEvaluacion"
                      class="form-control"
                      placeholder="2022-01-01"
                      required
                    />
                  </div>

                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      v-on:click="showModalFecha = false"
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
  props: ["idCurso"],
  data() {
    return {
      evaluacionesCurso: [],
      tiposEvaluaciones: [],
      evaluacionesFull: [],
      showModal: false,
      showModalFecha: false,
      nombreEvaluacion: "",
      tipoEvaluacion: "",
      porcentajeEvaluacion: "",
      fechaEvActual: null,
      fechaEvaluacion: "",
      modalIndex: "",
      idDocente: 0,
    };
  },

  mounted() {
    let identificacionCurso = this.idCurso;
    let identificacionUsuario = this.$store.getters.idUsuario;
    let that = this;
    axios
      .get(`http://localhost:8000/evaluaciones/${identificacionCurso}`)
      .then(function (response) {
        that.evaluacionesCurso = response.data;
      });

    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        that.idDocente = response.data.id;
      });

    axios
      .get("http://localhost:8000/evaluacion/tipos")
      .then(function (response) {
        that.tiposEvaluaciones = response.data;
      });

    // Comentario de Miguel: Para que sirve esto?
    axios.get(`http://localhost:8000/allInfoEvaluaciones/${identificacionCurso}`).then(function (response) {
      that.evaluacionesFull = response.data;
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
      let fecha = new Date(this.fechaEvActual);
      let fechaEntrega = new Date();

      // Se suman 14 dias desde la fecha tentativa de realización. Y se pasa a String del tipo YYYY-MM-DD
      fechaEntrega = new Date(fecha.getTime() + 14 * 24 * 60 * 60 * 1000);
      fechaEntrega = fechaEntrega.toISOString().slice(0, 10);

      // Se transforma el porcentaje 40% -> 0.4
      this.porcentajeEvaluacion = this.porcentajeEvaluacion / 100;

      axios
        .post("http://localhost:8000/add/evaluacion", {
          nombre: this.nombreEvaluacion,
          fechaEvActual: this.fechaEvActual,
          fechaEntrega: fechaEntrega,
          ponderacion: this.porcentajeEvaluacion,
          estado: "P",
          id_tipoEvaluacion: this.tipoEvaluacion,
          id_docente: this.idDocente,
          id_observacion: null,
          id_coordinacion: this.idCurso,
        })
        .then(function (response) {
          location.reload();
        });
    },
    modificarFecha: function (event, index) {
      console.log(this.evaluacionesFull[index]);
      let idFechaModificar = this.evaluacionesFull[index].id;
      let nuevaEvaluacion = {
        nombre: this.evaluacionesFull[index].nombre,
        fechaEvActual: this.fechaEvaluacion,
        fechaEntrega: this.evaluacionesFull[index].fechaEntrega,
        ponderacion: this.evaluacionesFull[index].ponderacion,
        estado: this.evaluacionesFull[index].estado,
        id_docente: this.evaluacionesFull[index].id_docente,
        id_observacion: this.evaluacionesFull[index].id_observacion,
        id_tipoEvaluacion: this.evaluacionesFull[index].id_tipoEvaluacion,
        id_coordinacion: this.evaluacionesFull[index].id_coordinacion,
      };
      console.log(nuevaEvaluacion);
      axios
        .put(
          `http://localhost:8000/update/evaluacion/${idFechaModificar}`,
          nuevaEvaluacion
        )
        .then(function (response) {
          location.reload();
        });
    },
  },
};
</script>

<style></style>
