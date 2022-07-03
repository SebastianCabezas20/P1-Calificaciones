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
            <th>Fecha de rendición</th>
            <th>Estado</th>
            <th class="row-Ponderacion">Pondera</th>
            <th class="row-ButtonIcon"></th>
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
            <!-- Calificacion de Evaluacion-->
            <td>
              <div class="text-center">
                <button
                  class="fa-solid fa-pencil botonTabla"
                  v-on:click="calificarEvaluacion($event, evaluacion.id)"
                  :disabled="evaluacion.estado == 'E'"
                  title="Ingresar calificaciones"
                ></button>
              </div>
            </td>
            <!-- Cambio de Ponderación. -->
            <td>
              <div class="text-center">
                <button
                  @click="(showModalPonderacion = true), (modalIndex = index)"
                  class="fa-solid fa-percent botonTabla"
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

      <EvaluacionesProvisorias
        v-if="
          evaluacionesCreadas.length !== 0 ||
          evaluacionesEliminadas.length !== 0 ||
          evaluacionesPonderacion.length !== 0
        "
        :evaluacionesCreadas="this.evaluacionesCreadas"
        :evaluacionesEliminadas="this.evaluacionesEliminadas"
        :evaluacionesPonderacion="this.evaluacionesPonderacion"
        :cambiosPonderacion="this.cambiosPonderacion"
        @EventGuardarCambios="() => guardarCambios()"
      />

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
                    <label class="form-label">Nombre</label>
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
                    <label for="fechaDeEvaluacion">Fecha de realización</label>
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
                    <button type="submit" class="btn btn-primary">
                      Crear
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
                    <label class="form-label"
                      >Anterior fecha de evaluación</label
                    >
                    <input
                      class="form-control"
                      type="date"
                      :value="this.evaluacionesCurso[modalIndex].fechaEvActual"
                      disabled
                    />
                  </div>
                  <div class="mb-3">
                    <label class="form-label">Nueva fecha de evaluación</label>
                    <input
                      v-model="nuevaFechaEvaluacion"
                      class="form-control"
                      type="date"
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
                    <label class="form-label">Ponderación actual</label>
                      <input
                        :value="this.evaluacionesInformacion[modalIndex].ponderacion * 100"
                        class="form-control"
                        disabled
                      />
                  </div>

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
import EvaluacionesProvisorias from "../../components/EvaluacionesProvisorias.vue";
import axios from "axios";
import moment from "moment";

export default {
  props: ["idAsignatura", "idCurso"],
  components: {
    Sidebar,
    Navbar,
    EvaluacionesProvisorias,
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

      evaluacionesCreadas: [],
      evaluacionesEliminadas: [],
      evaluacionesPonderacion: [],
      cambiosPonderacion: [],
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
    calificarEvaluacion: function (event, idEvaluacion) {
      this.$router.push({
        path: `/coordinador/curso/${this.idCurso}/add/calificacion/${idEvaluacion}`,
      });
    },

    guardarCambios() {
      let ponderacionTotal = 0;
      let coincidencia = 0;
      let modificada = 0;

      /* Ponderaciones de las evaluaciones actuales (No se suman las
      ponderaciones de aquellas evaluaciones que serán eliminadas y tampoco
      a aquellas que serán modificadas.). */
      for (var i = 0; i < this.evaluacionesInformacion.length; i++) {
        for (var j = 0; j < this.evaluacionesEliminadas.length; j++) {
          if (
            this.evaluacionesEliminadas[j].id ===
            this.evaluacionesInformacion[i].id
          ) {
            coincidencia++;
          }
        }
        for (var j = 0; j < this.evaluacionesPonderacion.length; j++) {
          if (
            this.evaluacionesPonderacion[j].nombre ===
            this.evaluacionesInformacion[i].nombre
          ) {
            ponderacionTotal =
              ponderacionTotal +
              parseFloat(this.evaluacionesPonderacion[j].ponderacion);
            modificada++;
          }
        }

        if (coincidencia === 0 && modificada === 0) {
          ponderacionTotal =
            ponderacionTotal +
            parseFloat(this.evaluacionesInformacion[i].ponderacion);
        }
        coincidencia = 0;
        modificada = 0;
      }

      /* Ponderacion de las nuevas evaluaciones (Se suman las
      ponderaciones de las evaluaciones que se agregarán) */
      for (var i = 0; i < this.evaluacionesCreadas.length; i++) {
        ponderacionTotal =
          ponderacionTotal +
          parseFloat(this.evaluacionesCreadas[i].ponderacion);
      }

      /* La ponderación se formatea para que de un valor que tenga
      maximo 3 decimales. */
      ponderacionTotal = parseFloat((ponderacionTotal * 100).toFixed(3));

      // Caso 1: Con las nuevas evaluaciones se sobrepasa el 100%.
      if (ponderacionTotal !== 100) {
        this.$swal.fire({
          icon: "error",
          title: "Suma de porcentajes de evaluación no permitidos",
          text: `La suma de ponderaciones del nuevo listado de evaluaciones da como resultado ${ponderacionTotal}%. Se espera que este valor sea 100%`,
        });
        return;
      }

      // Caso 2: El nuevo listado de evaluaciones da un 100%.
      else {

        // Coordinador elimina una evaluación de sus coordinaciones.
        for (var i = 0; i < this.evaluacionesEliminadas.length; i++) {
          let nombreEvaluacion = this.evaluacionesEliminadas[i].nombre;
          this.getEvaluacionesNombre(nombreEvaluacion).then(function (response) {
            let evaluacionesPorNombre = response;
            for (var i = 0; i < evaluacionesPorNombre.length; i++) {
              let idEvaluacionEliminar = evaluacionesPorNombre[i].id;
              axios.delete(`http://localhost:8000/delete/evaluacion/${idEvaluacionEliminar}`).then(function (response) {});
            }
          });
        }
        
        // Coordinador crea nuevas evaluaciones.
        for (var i = 0; i < this.evaluacionesCreadas.length; i++){
          for (var j = 0; j < this.coordinacionesAsignatura.length; j++) {
            let nuevaEvaluacion = {
              nombre: this.evaluacionesCreadas[i].nombre,
              fechaEvActual: this.evaluacionesCreadas[i].fechaEvActual,
              fechaEntrega: this.evaluacionesCreadas[i].fechaEntrega,
              ponderacion: this.evaluacionesCreadas[i].ponderacion,
              estado: this.evaluacionesCreadas[i].estado,
              obs_general: this.evaluacionesCreadas[i].obs_general,
              adjunto: this.evaluacionesCreadas[i].adjunto,
              id_tipoEvaluacion: this.evaluacionesCreadas[i].id_tipoEvaluacion,
              id_docente: this.coordinacionesAsignatura[j].id_docente.id,
              id_coordinacion: this.coordinacionesAsignatura[j].id_coordinacion.id,
            }
            axios
              .post("http://localhost:8000/add/evaluacion", nuevaEvaluacion)
              .then(function (response) {});
          }
        }

        // Coordinador modifica una evaluación en sus coordinaciones.
        for (var i = 0; i < this.evaluacionesPonderacion.length; i++) {
          let ponderacionEvaluacion =
            this.evaluacionesPonderacion[i].ponderacion;
          let nombreEvaluacion = this.evaluacionesPonderacion[i].nombre;

          let tuplaCambio = {
            ponderacionAnterior: this.cambiosPonderacion[i].ponderacionAnterior,
            ponderacionNueva: this.cambiosPonderacion[i].ponderacionNueva,
            motivo: this.cambiosPonderacion[i].motivo,
            fecha_cambio: this.cambiosPonderacion[i].fecha_cambio,
          };

          this.getEvaluacionesNombre(nombreEvaluacion).then(function (response) {
            let evaluacionesPorNombre = response;

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
                ponderacionAnterior: tuplaCambio.ponderacionAnterior,
                ponderacionNueva: tuplaCambio.ponderacionNueva,
                motivo: tuplaCambio.motivo,
                fecha_cambio: tuplaCambio.fecha_cambio,
                id_evaluacion: evaluacionesPorNombre[i].id,
              };

              let idEvaluacionCambio = evaluacionesPorNombre[i].id;

              // Requests
              axios.put(`http://localhost:8000/update/evaluacion/${idEvaluacionCambio}`, nuevaEvaluacion).then(function (response) {});
              axios.post("http://localhost:8000/add/cambioPonderacion", tuplaCambioPonderacion).then(function (response) {});
            }
          });
        }

        this.$swal.fire({
          icon: "success",
          title: "Listado de evaluaciones modificado exitosamente",
          text: "Las evaluaciones de la actual coordinación fueron actualizadas satisfactoriamente",
        })
        .then((result) => {
          location.reload();
        });
      }
    },

    deleteEvaluacion: function (event, index) {
      /*  Se comprueba si la evaluación que seleccionó el coordinador para
      eliminar ya está considerada para ser eliminada. */
      if (
        this.evaluacionesEliminadas.includes(
          this.evaluacionesInformacion[index]
        )
      ) {
        this.$swal.fire({
          icon: "error",
          title: "Evaluación eliminada",
          text: "La evaluación ya está considerada para ser eliminada.",
        });
        return;
      }
      // Sino, se agrega para posteriormente ser eliminada.
      this.evaluacionesEliminadas.push(this.evaluacionesInformacion[index]);

      // Método anterior.

      /* let idEvaluacionEliminar = 0;

      let nombreEvaluacion = this.evaluacionesInformacion[index].nombre;
      let that = this;
      this.getEvaluacionesNombre(nombreEvaluacion).then(function (response) {
        let evaluacionesPorNombre = response;
        console.log(evaluacionesPorNombre);

        for (var i = 0; i < evaluacionesPorNombre.length; i++) {
          idEvaluacionEliminar = evaluacionesPorNombre[i].id;

          axios
            .delete(
              `http://localhost:8000/delete/evaluacion/${idEvaluacionEliminar}`
            )
            .then(function (response) {});
        }

        location.reload();
      });  */
    },

    // Coordinador crea una evaluación en todas las coordinaciones de su asignatura.
    crearEvaluacion: function (event) {
      // Se transforma el porcentaje 40% -> 0.4
      let porcentajeEvaluacionIngresado = this.porcentajeEvaluacion / 100;

      // Caso 1: La fecha ingresada es igual o menor a la fecha actual.
      if (moment().startOf("day") >= moment(this.fechaEvActual)) {
        this.$swal.fire({
          icon: "error",
          title: "Fecha de evaluación no permitida.",
          text: "La fecha de realización de la evaluación debe ser mayor a la fecha actual",
        });
      }

      // Caso 2: Es posible agregar la evaluación.
      else {
        let fecha = new Date(this.fechaEvActual);
        let fechaEntrega = new Date();
        let that = this;

        // Se suman 14 dias desde la fecha tentativa de realización. Y se pasa a String del tipo YYYY-MM-DD
        fechaEntrega = new Date(fecha.getTime() + 14 * 24 * 60 * 60 * 1000);
        fechaEntrega = fechaEntrega.toISOString().slice(0, 10);

        /* La nueva evaluación se agrega sin los id de docente y coordinación,
        puesto que estos se agregan al guardar los cambios. */
        let nuevaEvaluacion = {
          nombre: this.nombreEvaluacion,
          fechaEvActual: this.fechaEvActual,
          fechaEntrega: fechaEntrega,
          ponderacion: porcentajeEvaluacionIngresado,
          estado: "P",
          obs_general: "",
          adjunto: null,
          id_tipoEvaluacion: this.tipoEvaluacion,
          id_docente: 0,
          id_coordinacion: 0,
        };

        this.evaluacionesCreadas.push(nuevaEvaluacion);
      }
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

      // Cálculo de la nueva fecha de entrega.
      let fecha = new Date(this.nuevaFechaEvaluacion);
      let nuevaFechaEntrega = new Date();
      nuevaFechaEntrega = new Date(fecha.getTime() + 14 * 24 * 60 * 60 * 1000);
      nuevaFechaEntrega = nuevaFechaEntrega.toISOString().slice(0, 10);

      /* Caso 1: La nueva fecha ingresada es igual o menor a la fecha actual. */
      if (moment().startOf("day") >= moment(this.nuevaFechaEvaluacion)) {
        this.$swal.fire({
          icon: "error",
          title: "Fecha de evaluación no permitida.",
          text: "La nueva fecha de realización de la evaluación debe ser mayor a la fecha actual",
        });
      } else if (
        /* Caso 2: La nueva fecha de evaluación es manor o igual a la fecha
      original de evaluación. (Se preguntará a los clientes si esto es un error o no.)*/
        moment(fechaEvaluacionOriginal) >= moment(this.nuevaFechaEvaluacion)
      ) {
        this.$swal.fire({
          icon: "error",
          title: "Fecha de evaluación no permitida.",
          text: "La nueva fecha de realización de la evaluación debe ser mayor a la fecha original de realización",
        });
      } else {
        /* Todo correcto. */
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
            let fechaActual = new Date();
            fechaActual = fechaActual.toISOString().slice(0, 10);
            let tuplaCambioFecha = {
              fechaAnterior: fechaEvaluacionOriginal,
              fechaNueva: that.nuevaFechaEvaluacion,
              motivo: that.motivoCambioFecha,
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
                    "http://localhost:8000/add/cambioFecha",
                    tuplaCambioFecha
                  )
                  .then(function (responseThird) {});
              });
          }
        });
        this.$swal
          .fire({
            icon: "success",
            title: "Fecha de evaluación actualizada",
            text: "La fecha de evaluación fue modificada satisfactoriamente",
          })
          .then((result) => {
            location.reload();
          });
      }
    },

    modificarPonderacion(event, indexClic) {
      // Se verifica si la evaluación ya está considerada para ser modificada.
      let modificada = 0;
      for (var i = 0; i < this.evaluacionesPonderacion.length; i++) {
        if (
          this.evaluacionesPonderacion[i].nombre ===
          this.evaluacionesInformacion[indexClic].nombre
        ) {
          modificada++;
        }
      }

      // Caso 1: La evaluación está considerada para ser eliminada.
      if (
        this.evaluacionesEliminadas.includes(
          this.evaluacionesInformacion[indexClic]
        )
      ) {
        this.$swal.fire({
          icon: "error",
          title: "Evaluación eliminada",
          text: "La evaluación ya está considerada para ser eliminada.",
        });
        return;
      }

      // Caso 2: La evaluación ya recibió el cambio de ponderación.
      else if (modificada !== 0) {
        this.$swal.fire({
          icon: "error",
          title: "Evaluación modificada",
          text: "La evaluación ya está considerada para ser modificada.",
        });
        return;
      }

      // Caso 3: Es posible modificar la ponderación.
      else {
        let ponderacionEvaluacion = this.nuevaPonderacionEv / 100;
        let ponderacionAnterior =
          this.evaluacionesInformacion[indexClic].ponderacion;
        let fechaActual = new Date();
        fechaActual = fechaActual.toISOString().slice(0, 10);

        /* Se agrega solo la evaluación de la coordinación actual. Al guardar
        los cambios se debe cambiar en todas las coordinaciones espejos si existen */
        let nuevaEvaluacion = {
          nombre: this.evaluacionesInformacion[indexClic].nombre,
          fechaEvActual: this.evaluacionesInformacion[indexClic].fechaEvActual,
          fechaEntrega: this.evaluacionesInformacion[indexClic].fechaEntrega,
          ponderacion: ponderacionEvaluacion,
          estado: this.evaluacionesInformacion[indexClic].estado,
          obs_general: this.evaluacionesInformacion[indexClic].obs_general,
          adjunto: this.evaluacionesInformacion[indexClic].adjunto,
          id_tipoEvaluacion:
            this.evaluacionesInformacion[indexClic].id_tipoEvaluacion,
        };

        let tuplaCambioPonderacion = {
          ponderacionAnterior: ponderacionAnterior,
          ponderacionNueva: ponderacionEvaluacion,
          motivo: this.motivoCambioPonderacion,
          fecha_cambio: fechaActual,
        };

        this.evaluacionesPonderacion.push(nuevaEvaluacion);
        this.cambiosPonderacion.push(tuplaCambioPonderacion);
      }

      // Método anterior.
      /*
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

        // En la tabla Evaluación, se buscan las evaluaciones con un nombre especifico
        // y que pertenezcan a una misma asignatura, lo que provoca que se actualice
        // esa evaluación en todas las coordinaciones asociadas a esa asignatura.
        this.getEvaluacionesNombre(nombreEvaluacion).then(function (response) {
          let evaluacionesPorNombre = response;

          // Cada una de las evaluaciones se va modificando y además, se
          // registra el cambio de ponderación.
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
      } */
    },
  },
};
</script>

<style></style>
