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
            <td>
              <div class="text-center">
                <button
                  class="fa-solid fa-gear botonTabla"
                  v-on:click="modificarCalificacion($event, evaluacion.id)"
                  :disabled="evaluacion.estado == 'P'"
                  title="Modificar calificaciones"
                ></button>
              </div>
            </td>
            <td>
              <div class="text-center">
                <button
                  @click="abrirCambioFecha(index)"
                  class="fa-solid fa-calendar botonTabla"
                  :disabled="
                    evaluacion.id_coordinacion.id_asignatura.isAutogestionada ==
                      false || evaluacion.estado == 'E'
                  "
                  title="Modificar fecha de evaluación"
                ></button>
              </div>
            </td>
            <td>
              <div class="text-center">
                <button
                  v-if="this.evaluacionesEliminadas.includes(evaluacion)"
                  class="fa-solid fa-trash-can botonTabla"
                  style="background-color: red;"
                  v-on:click="deleteEvaluacion($event, index)"
                  :disabled="
                    evaluacion.id_coordinacion.id_asignatura.isAutogestionada ==
                      false || evaluacion.estado == 'E'
                  "
                  title="Eliminar evaluación"
                ></button>
                <button
                  v-else
                  class="fa-solid fa-trash-can botonTabla"
                  v-on:click="deleteEvaluacion($event, index)"
                  :disabled="
                    evaluacion.id_coordinacion.id_asignatura.isAutogestionada ==
                      false || evaluacion.estado == 'E'
                  "
                  title="Eliminar evaluación"
                ></button>
              </div>
            </td>
            <td>
              <div class="text-center">
                <button
                  class="fa-solid fa-pencil-can botonTabla"
                  v-on:click="sendEmail(index)"
                  title="Prueba mail"
                ></button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Botón que abre el modal para agregar una evaluación. -->
      <template
        v-for="informacion in informacionCoordinacion"
        :key="informacion.id"
      >
        <button
          @click="showModal = true"
          type="button"
          class="submitButton"
          :disabled="informacion.id_asignatura.isAutogestionada == false"
        >
          Agregar evaluación
        </button>
      </template>

      <EvaluacionesProvisorias
        v-if = "evaluacionesCreadas.length !== 0 || evaluacionesEliminadas.length !== 0"
        :evaluacionesCreadas = 'this.evaluacionesCreadas'
        :evaluacionesEliminadas = 'this.evaluacionesEliminadas'
        @EventGuardarCambios = "() => guardarCambios()"
      />

      <!-- Modal para crear una evaluación -->
      <transition name="fase" appear>
        <div class="modal-overlay" v-if="showModal">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">
                  Crear evaluación
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
                    <label for="fechaDeEvaluacion"
                      >Fecha de realización</label
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
                      type="number"
                      min="1"
                      max="100"
                      step="0.1"
                      required
                    />
                  </div>
                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      v-on:click="showModal = false"
                    >
                      Cerrar
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
                <h5 class="modal-title" id="exampleModalLabel">
                  Modificar fecha de evaluación
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
                      >Anterior fecha de evaluación</label
                    >
                    <input
                      class="form-control"
                      type="date"
                      :value="this.evaluacionesFull[modalIndex].fechaEvActual"
                      disabled
                    />
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Nueva fecha de evaluación</label>
                    <input
                      v-model="fechaEvaluacion"
                      class="form-control"
                      type="date"
                      required
                    />
                  </div>

                  <div id="divMotivo">
                    <h5 class="textoFormulario">Motivo del cambio de fecha</h5>
                    <textarea
                      class="form-control"
                      rows="5"
                      required
                      placeholder="Escriba acá el motivo del cambio de fecha."
                      id="motivoCambio"
                      v-model="motivoCambio"
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
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import EvaluacionesProvisorias from "../../components/EvaluacionesProvisorias.vue";
import axios from "axios";
import emailjs from 'emailjs-com';
import moment from 'moment';

export default {
  components: {
    Sidebar,
    Navbar,
    EvaluacionesProvisorias,
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
      motivoCambio: "",
      informacionCoordinacion: [],
      mailDocente: "",
      nombreDocente: "",
      mail_mail: "",
      mail_evaluacion: "",
      mail_docente: "",
      mail_fecha: "",

      evaluacionesCreadas: [],
      evaluacionesEliminadas: [],
    };
  },

  mounted() {
    let identificacionCurso = this.idCurso;
    let identificacionUsuario = this.$store.getters.idUsuario;
    this.nombreDocente = this.$store.getters.nameUser;
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

    axios
      .get(`http://localhost:8000/allInfoEvaluaciones/${identificacionCurso}`)
      .then(function (response) {
        that.evaluacionesFull = response.data;
      });

    axios
      .get(`http://localhost:8000/get/coordinacion/${identificacionCurso}`)
      .then(function (response) {
        that.informacionCoordinacion = response.data;
      });
  },

  methods: {
    abrirCambioFecha(index) {
      this.modalIndex = index;
      this.showModalFecha = true;
    },

    deleteEvaluacion: function (event, index) {      
      /*  Se comprueba si la evaluación que seleccionó para eliminar ya está 
      considerada para ser eliminada. */
      if(this.evaluacionesEliminadas.includes(this.evaluacionesCurso[index])) {
        this.$swal.fire({
          icon: "error",
          title: "Evaluación eliminada",
          text: "La evaluación ya está considerada para ser eliminada.",
        });
        return;
      }
      // Sino, se agrega para posteriormente ser eliminada.
      this.evaluacionesEliminadas.push(this.evaluacionesCurso[index]);
    },

    crearEvaluacion: function (event) {
      // Se transforma el porcentaje 40% -> 0.4
      let porcentajeEvaluacionIngresado = this.porcentajeEvaluacion / 100;

      // Caso 1: La fecha ingresada es igual o menor a la fecha actual.
      if (moment().startOf('day') >= moment(this.fechaEvActual)){
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

        // Metodo 2: Considera validación de ponderaciones.
        let nuevaEvaluacion = {
          nombre: this.nombreEvaluacion,
          fechaEvActual: this.fechaEvActual,
          fechaEntrega: fechaEntrega,
          ponderacion: porcentajeEvaluacionIngresado,
          estado: "P",
          obs_general: "",
          adjunto: null,
          id_tipoEvaluacion: this.tipoEvaluacion,
          id_docente: this.idDocente,
          id_coordinacion: this.idCurso,
        }
        this.evaluacionesCreadas.push(nuevaEvaluacion);
      }
    },

    guardarCambios() {
      let ponderacionTotal = 0;
      let coincidencia = 0;
      
      /* Ponderaciones de las evaluaciones actuales (No se suman las 
      ponderaciones de aquellas evaluaciones que serán eliminadas). */
      for (var i = 0; i < this.evaluacionesCurso.length; i++) {
        for (var j = 0; j < this.evaluacionesEliminadas.length; j++) {
          if(this.evaluacionesEliminadas[j].id === this.evaluacionesCurso[i].id){
            coincidencia++
          }
        }
        if(coincidencia === 0){
          ponderacionTotal = ponderacionTotal + parseFloat(this.evaluacionesCurso[i].ponderacion);
        }
        coincidencia = 0 
      }

      /* Ponderacion de las nuevas evaluaciones (Se suman las 
      ponderaciones de las evaluaciones que se agregarán) */
      for (var i = 0; i < this.evaluacionesCreadas.length; i++) {
        ponderacionTotal = ponderacionTotal + parseFloat(this.evaluacionesCreadas[i].ponderacion);
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
        return ;
      }
      
      // Caso 2: El nuevo listado de evaluaciones da un 100%.
      else {
        for (var i = 0; i < this.evaluacionesCreadas.length; i++){
          axios.post("http://localhost:8000/add/evaluacion", this.evaluacionesCreadas[i])
          .then(function (response) {});
        }

        for (var i = 0; i < this.evaluacionesEliminadas.length; i++){
          axios.delete(`http://localhost:8000/delete/evaluacion/${this.evaluacionesEliminadas[i].id}`)
          .then(function (response) {});
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

    modificarFecha: function (event, index) {
      // Cálculo de la nueva fecha de entrega.
      let fecha = new Date(this.fechaEvaluacion);
      let fechaEntrega = new Date();
      fechaEntrega = new Date(fecha.getTime() + 14 * 24 * 60 * 60 * 1000);
      fechaEntrega = fechaEntrega.toISOString().slice(0, 10);

      // Otras variables a utilizar.
      let idFechaModificar = this.evaluacionesFull[index].id;
      let fechaOriginal = this.evaluacionesFull[index].fechaEvActual;

      /* Caso 1: La nueva fecha ingresada es igual o menor a la fecha actual. */
      if (moment().startOf('day') >= moment(this.fechaEvaluacion)){
        this.$swal.fire({
          icon: "error",
          title: "Fecha de evaluación no permitida.",
          text: "La nueva fecha de realización de la evaluación debe ser mayor a la fecha actual",
        });
      }

      /* Caso 2: La nueva fecha de evaluación es manor o igual a la fecha 
      original de evaluación. (Se preguntará a los clientes si esto es un error o no.)*/
      else if (moment(fechaOriginal) >= moment(this.fechaEvaluacion)) {
        this.$swal.fire({
          icon: "error",
          title: "Fecha de evaluación no permitida.",
          text: "La nueva fecha de realización de la evaluación debe ser mayor a la fecha original de realización",
        });
      }

      /* Todo correcto. */
      else {
        let that = this;

        let nuevaEvaluacion = {
        nombre: this.evaluacionesFull[index].nombre,
        fechaEvActual: this.fechaEvaluacion,
        fechaEntrega: fechaEntrega,
        ponderacion: this.evaluacionesFull[index].ponderacion,
        estado: this.evaluacionesFull[index].estado,
        obs_general: this.evaluacionesFull[index].obs_general,
        adjunto: this.evaluacionesFull[index].adjunto,
        id_docente: this.evaluacionesFull[index].id_docente,
        id_tipoEvaluacion: this.evaluacionesFull[index].id_tipoEvaluacion,
        id_coordinacion: this.evaluacionesFull[index].id_coordinacion,
      };

      let cambioFecha = {
        fechaAnterior: fechaOriginal,
        fechaNueva: this.fechaEvaluacion,
        motivo: this.motivoCambio,
        id_evaluacion: this.evaluacionesFull[index].id,
      };

      // Requests.
      axios
        .put(
          `http://localhost:8000/update/evaluacion/${idFechaModificar}`,
          nuevaEvaluacion
        )
        .then(function (response) {
        });
      axios
        .post("http://localhost:8000/add/cambioFecha", cambioFecha)
        .then(function (response) {
          that.$swal.fire({
            icon: "success",
            title: "Fecha de evaluación actualizada",
            text: "La fecha de evaluación fue modificada satisfactoriamente",
          })
          .then((result) => {
            location.reload();
          });
        });
      }
    },

    calificarEvaluacion: function (event, idEvaluacion) {
      this.$router.push({
        path: `/docente/curso/${this.idCurso}/add/calificacion/${idEvaluacion}`,
      });
    },

    modificarCalificacion: function (event, idEvaluacion) {
      this.$router.push({
        path: `/docente/curso/${this.idCurso}/evaluacion/${idEvaluacion}`,
      });
    },
    
    sendEmail(index) {
      this.mailDocente = this.$store.getters.email;
      console.log(this.mailDocente);
      emailjs.send('pingeso', 'template_evaluacion', {
        mail_mail: this.mailDocente,
        mail_evaluacion: this.evaluacionesFull[index].nombre,
        mail_docente: this.nombreDocente,
        mail_fecha: this.evaluacionesFull[index].fechaEvActual
      },
      'TIAwArj4Go2oOAbqv')
      .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
      }, function(error) {
        console.log('FAILED...', error);
      });
    },
  },
};
</script>

<style></style>
