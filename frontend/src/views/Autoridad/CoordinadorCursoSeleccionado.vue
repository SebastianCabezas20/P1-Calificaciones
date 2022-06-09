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
        <h3 class="textTitleV2">Evaluaciones</h3>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th>Evaluación</th>
            <th>Tipo</th>
            <th>Fecha de Rendición</th>
            <th>Estado</th>
            <th class="row-Ponderacion">Pondera</th>
            <th class="row-ButtonIcon"></th>
            <th class="row-ButtonIcon"></th>
            <th class="row-ButtonIcon"></th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(evaluacion, index) in evaluacionesCurso" :key="index">
            <td>{{ evaluacion.nombre }}</td>
            <td>{{ evaluacion.id_tipoEvaluacion.nombre }}</td>
            <td>{{ evaluacion.fechaEvActual }}</td>
            <td v-if="evaluacion.estado == 'E'">Evaluada</td>
            <td v-else>Pendiente</td>
            <td>{{ evaluacion.ponderacion * 100 }}%</td>
            <!-- Cambio de Ponderación. -->
            <td>
              <div class="text-center">
                <button
                  @click="(showModalPonderacion = true), (modalIndex = index)"
                  class="fa-solid fa-percent botonTabla"
                  :disabled="evaluacion.estado == 'E'"
                  title="Modificar la ponderación de la evaluación."
                ></button>
              </div>
            </td>
            <!-- Cambio en la fecha de evaluación. -->
            <td>
              <div class="text-center">
                <button
                  @click="(showModalFecha = true), (modalIndex = index)"
                  class="fa-solid fa-calendar botonTabla"
                  :disabled="evaluacion.estado == 'E'"
                  title="Modificar fecha de evaluación"
                ></button>
              </div>
            </td>
            <!-- Eliminar una evaluación. -->
            <td>
              <div class="text-center">
                <button
                  class="fa-solid fa-trash-can botonTabla"
                  v-on:click="deleteEvaluacion($event, index)"
                  :disabled="evaluacion.estado == 'E'"
                  title="Eliminar evaluación"
                ></button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Botón que abre el modal para agregar una evaluación. -->
      <button @click="showModalAdd = true" type="button" class="submitButton">
        Agregar evaluación
      </button>

      <!-- Modal para agregar evaluación -->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModalAdd">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Crear evaluación</h5>
                <button
                  type="button"
                  class="btn-close"
                  @click="showModalAdd = false"
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
                    <label class="form-label">Tipo de evaluación</label>
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
                      v-on:click="showModalAdd = false"
                    >
                      Cancelar
                    </button>
                    <button
                      @click="showModalAdd = false"
                      type="submit"
                      class="btn btn-primary"
                    >
                      Guardar cambios
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
                <h5 class="modal-title">Modificar fecha de evaluación</h5>
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
                    <label class="form-label">Nueva fecha de evaluación</label>
                    <input
                      v-model="nuevaFechaEvaluacion"
                      class="form-control"
                      placeholder="2022-01-01"
                      required
                    />
                  </div>

                  <div id="divMotivo">
                    <h5 class="textoFormulario">Motivo del cambio de fecha</h5>
                    <textarea
                      rows="9"
                      placeholder="Escriba acá el motivo del cambio de fecha."
                      id="motivoCambioFecha"
                      required
                      v-model="motivoCambioFecha"
                      style="width: 450px"
                    ></textarea>
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
                      Guardar cambios
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- Modal para modificar la ponderación de una evaluación. -->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModalPonderacion">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">
                  Modificar ponderación de la evaluación
                </h5>
                <button
                  type="button"
                  class="btn-close"
                  @click="showModalPonderacion = false"
                ></button>
              </div>

              <div class="modal-body">
                <form
                  action="#"
                  method="PUT"
                  v-on:submit.prevent="modificarPonderacion($event, modalIndex)"
                >
                  <div class="mb-3">
                    <label class="form-label">Nueva ponderación</label>
                    <input
                      v-model="nuevaPonderacionEv"
                      class="form-control"
                      placeholder="15"
                      type="number"
                      min="1"
                      max="100"
                      step="0.1"
                      required
                    />
                  </div>

                  <div id="divMotivo">
                    <h5 class="textoFormulario">
                      Motivo del cambio de ponderación.
                    </h5>
                    <textarea
                      rows="9"
                      placeholder="Escriba acá el motivo del cambio de ponderación."
                      id="motivoCambioPonderacion"
                      required
                      v-model="motivoCambioPonderacion"
                      style="width: 450px"
                    ></textarea>
                  </div>

                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      v-on:click="showModalPonderacion = false"
                    >
                      Cancelar
                    </button>
                    <button type="submit" class="btn btn-primary">
                      Guardar cambios
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
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";

export default {
  props: ["idAsignatura", "idCurso"],
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      evaluacionesCurso: [],
      tiposEvaluaciones: [],
      coordinacionesAsignatura: [],
      evaluacionesInformacion: [],
      showModalAdd: false,
      showModalFecha: false,
      showModalPonderacion: false,
      modalIndex: "",

      // V-Models
      nombreEvaluacion: "",
      tipoEvaluacion: 0,
      fechaEvActual: "",
      porcentajeEvaluacion: "",
      nuevaFechaEvaluacion: "",
      motivoCambioFecha: "",
      nuevaPonderacionEv: null,
      motivoCambioPonderacion: "",
    };
  },

  mounted() {
    let identificacionCurso = this.idCurso;
    let identificacionAsignatura = this.idAsignatura;
    let identificacionUsuario = this.$store.getters.idUsuario;
    let that = this;

    axios
      .get(`http://localhost:8000/evaluaciones/${identificacionCurso}`)
      .then(function (response) {
        that.evaluacionesCurso = response.data;
      });

    axios
      .get("http://localhost:8000/evaluacion/tipos")
      .then(function (response) {
        that.tiposEvaluaciones = response.data;
      });

    axios
      .get(
        `http://localhost:8000/coordinaciones/asignatura/${identificacionAsignatura}`
      )
      .then(function (response) {
        that.coordinacionesAsignatura = response.data;
      });

    axios
      .get(`http://localhost:8000/allInfoEvaluaciones/${identificacionCurso}`)
      .then(function (response) {
        that.evaluacionesInformacion = response.data;
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

    // Coordinador crea una evaluación en todas las coordinaciones de su asignatura.
    crearEvaluacion: function (event) {
      let fecha = new Date(this.fechaEvActual);
      let fechaEntrega = new Date();
      fechaEntrega = new Date(fecha.getTime() + 14 * 24 * 60 * 60 * 1000);
      fechaEntrega = fechaEntrega.toISOString().slice(0, 10);
      this.porcentajeEvaluacion = this.porcentajeEvaluacion / 100;

      for (var i = 0; i < this.coordinacionesAsignatura.length; i++) {
        let nuevaEvaluacion = {
          nombre: this.nombreEvaluacion,
          fechaEvActual: this.fechaEvActual,
          fechaEntrega: fechaEntrega,
          ponderacion: this.porcentajeEvaluacion,
          estado: "P",
          obs_general: "",
          adjunto: null,
          id_tipoEvaluacion: this.tipoEvaluacion,
          id_docente: this.coordinacionesAsignatura[i].id_docente.id,
          id_coordinacion: this.coordinacionesAsignatura[i].id_coordinacion.id,
        };
        axios
          .post("http://localhost:8000/add/evaluacion", nuevaEvaluacion)
          .then(function (response) {});
      }
      location.reload();
    },

    // Función para obtener las evaluaciones iguales de una asignatura.
    async getEvaluacionesNombre(nombreEvaluacion) {
      const response = await axios.get(
        `http://localhost:8000/get/evaluaciones/${nombreEvaluacion}/asignatura/${this.idAsignatura}`
      );
      return response.data;
    },

    modificarFecha(event, indexClic) {
      // Datos para el registro.
      let fechaEvaluacionOriginal =
        this.evaluacionesInformacion[indexClic].fechaEvActual;
      let idEvaluacion = this.evaluacionesInformacion[indexClic].id;

      console.log(this.evaluacionesInformacion[indexClic]);

      // Cálculo de la nueva fecha de entrega.
      let fecha = new Date(this.nuevaFechaEvaluacion);
      let nuevaFechaEntrega = new Date();
      nuevaFechaEntrega = new Date(fecha.getTime() + 14 * 24 * 60 * 60 * 1000);
      nuevaFechaEntrega = nuevaFechaEntrega.toISOString().slice(0, 10);

      let nombreEvaluacion = this.evaluacionesInformacion[indexClic].nombre;
      let that = this;
      this.getEvaluacionesNombre(nombreEvaluacion).then(function (response) {
        let evaluacionesPorNombre = response;

        for (var i = 0; i < evaluacionesPorNombre.length; i++) {
          let nuevaEvaluacion = {
            nombre: evaluacionesPorNombre[i].nombre,
            fechaEvActual: that.nuevaFechaEvaluacion,
            fechaEntrega: nuevaFechaEntrega,
            ponderacion: evaluacionesPorNombre[i].ponderacion,
            estado: evaluacionesPorNombre[i].estado,
            obs_general: evaluacionesPorNombre[i].obs_general,
            adjunto: evaluacionesPorNombre[i].adjunto,
            id_docente: evaluacionesPorNombre[i].id_docente,
            id_tipoEvaluacion: evaluacionesPorNombre[i].id_tipoEvaluacion,
            id_coordinacion: evaluacionesPorNombre[i].id_coordinacion,
          };

          let tuplaCambioFecha = {
            fechaAnterior: fechaEvaluacionOriginal,
            fechaNueva: that.nuevaFechaEvaluacion,
            motivo: that.motivoCambioFecha,
            id_evaluacion: evaluacionesPorNombre[i].id,
          };

          let idEvaluacionCambio = evaluacionesPorNombre[i].id;

          // Requests
          axios
            .put(
              `http://localhost:8000/update/evaluacion/${idEvaluacionCambio}`,
              nuevaEvaluacion
            )
            .then(function (responseTwo) {
              axios
                .post("http://localhost:8000/add/cambioFecha", tuplaCambioFecha)
                .then(function (responseThird) {});
            });
        }
      });
      location.reload();
    },
    modificarPonderacion(event, indexClic) {
      // Se transforma el porcentaje 40% -> 0.4
      let ponderacionEvaluacion = this.nuevaPonderacionEv / 100;

      // Se comprueba que no se sobrepase el 100% (Incluyendo las evaluaciones evaluadas).
      let ponderacionTotal = 0;
      for (var i = 0; i < this.evaluacionesInformacion.length; i++) {
        if (i == indexClic) {
          ponderacionTotal = ponderacionTotal + ponderacionEvaluacion;
        } else {
          ponderacionTotal =
            ponderacionTotal +
            parseFloat(this.evaluacionesInformacion[i].ponderacion);
        }
      }

      // Caso 1: Con la nueva ponderación se sobrepasa el 100%
      if (ponderacionTotal > 1) {
        this.$swal.fire({
          icon: "error",
          title: "Porcentaje de evaluación no permitido",
          text: "El porcentaje ingresado sobrepasa el 100% total permitido",
        });
      }

      // Caso 2: No se sobrepasa.
      else {
        // Datos para el registro.
        let ponderacionAnterior =
          this.evaluacionesInformacion[indexClic].ponderacion;
        let idEvaluacion = this.evaluacionesInformacion[indexClic].id;
        let nombreEvaluacion = this.evaluacionesInformacion[indexClic].nombre;
        let fechaActual = new Date();
        fechaActual = fechaActual.toISOString().slice(0, 10);
        let that = this;

        /* En la tabla Evaluación, se buscan las evaluaciones con un nombre especifico
        y que pertenezcan a una misma asignatura, lo que provoca que se actualice
        esa evaluación en todas las coordinaciones asociadas a esa asignatura. */
        this.getEvaluacionesNombre(nombreEvaluacion).then(function (response) {
          let evaluacionesPorNombre = response;
          console.log(evaluacionesPorNombre);

          /* Cada una de las evaluaciones se va modificando y además, se 
          registra el cambio de ponderación. */
          for (var i = 0; i < evaluacionesPorNombre.length; i++) {
            let nuevaEvaluacion = {
              nombre: evaluacionesPorNombre[i].nombre,
              fechaEvActual: evaluacionesPorNombre[i].fechaEvActual,
              fechaEntrega: evaluacionesPorNombre[i].fechaEntrega,
              ponderacion: ponderacionEvaluacion,
              estado: evaluacionesPorNombre[i].estado,
              obs_general: evaluacionesPorNombre[i].obs_general,
              adjunto: evaluacionesPorNombre[i].adjunto,
              id_docente: evaluacionesPorNombre[i].id_docente,
              id_tipoEvaluacion: evaluacionesPorNombre[i].id_tipoEvaluacion,
              id_coordinacion: evaluacionesPorNombre[i].id_coordinacion,
            };

            let tuplaCambioPonderacion = {
              ponderacionAnterior: ponderacionAnterior,
              ponderacionNueva: ponderacionEvaluacion,
              motivo: that.motivoCambioPonderacion,
              fecha_cambio: fechaActual,
              id_evaluacion: evaluacionesPorNombre[i].id,
            };

            let idEvaluacionCambio = evaluacionesPorNombre[i].id;

            // Requests
            axios
              .put(
                `http://localhost:8000/update/evaluacion/${idEvaluacionCambio}`,
                nuevaEvaluacion
              )
              .then(function (responseTwo) {
                axios
                  .post(
                    "http://localhost:8000/add/cambioPonderacion",
                    tuplaCambioPonderacion
                  )
                  .then(function (responseThird) {
                    that.$swal
                      .fire({
                        icon: "success",
                        title: "Modificación exitosa",
                        text: `La evaluacion ${nombreEvaluacion} fue modificada satisfactoriamente. La nueva ponderación de la evaluación es ${
                          ponderacionEvaluacion * 100
                        }%`,
                      })
                      .then((result) => {
                        location.reload();
                      });
                  });
              });
          }
        });
      }
    },
  },
};
</script>

<style></style>
