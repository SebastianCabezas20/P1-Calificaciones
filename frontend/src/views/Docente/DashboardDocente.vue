<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="row" style="background-color: #ffffff">
        <!-- Cuadro con las coordinaciones inscritas por el docente. -->
        <div
          class="col cuadradoDashboard"
          style="margin-right: 20px"
          @click="coordinaciones()"
        >
          <div class="iconoDashboard">
            <span class="fa-solid fa-book fa-3x"></span>
          </div>
          <h2>Coordinaciones inscritas este semestre</h2>
          <p>Totales (teoría - laboratorio)</p>
          <h3>
            {{ coordinacionesTotales }} ({{ coordinacionesTeoria }} -
            {{ coordinacionesLaboratorio }})
          </h3>
        </div>

        <!-- Cuadro con solicitudes pendientes y recibidas. -->
        <div
          class="col cuadradoDashboard"
          style="margin-left: 20px"
          @click="solicitudes()"
        >
          <div class="iconoDashboard">
            <span class="fa-solid fa-file-circle-exclamation fa-3x"></span>
          </div>
          <h2>Solicitudes de revisión pendientes</h2>
          <p>Pendientes - recibidas</p>
          <h3>{{ solicitudesPendientes }} - {{ solicitudesTotales }}</h3>
        </div>
      </div>

      <!-- Cuadro que muestra las tres próximas entregas de notas. -->
      <div class="row" style="background-color: #ffffff">
        <div class="col rectanguloDashboard">
          <h2>Próximas entregas de calificaciones</h2>
          <TablaEvaluaciones
            :evaluaciones="this.evPendientesEntrega"
            @EventIngresarEvaluacion="(index) => ingresarEvaluacion(index)"
          />
        </div>
      </div>

      <!-- Cuadro que muestra las evaluaciones que se encuentran fuera del 
        plazo de entrega de notas. -->
      <div class="row" style="background-color: #ffffff">
        <div class="col rectanguloDashboard">
          <h2>Entrega de calificaciones fuera de plazo</h2>
          <TablaEvaluaciones
            :evaluaciones="this.evFueraEntrega"
            @EventIngresarEvaluacion="(index) => ingresarEvaluacion(index)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import moment from "moment";
import TablaEvaluaciones from "../../components/TablaEvaluacionesBasica.vue";

export default {
  components: {
    Sidebar,
    Navbar,
    TablaEvaluaciones,
  },
  data() {
    return {
      solicitudesPendientes: 0,
      solicitudesTotales: 0,
      coordinacionesTotales: 0,
      coordinacionesTeoria: 0,
      coordinacionesLaboratorio: 0,
      evPendientesEntrega: [],
      evFueraEntrega: [],
    };
  },
  mounted() {
    let identificacionUsuario = this.$store.getters.idUsuario;
    let that = this;
    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        let idDocente = response.data.id;

        /* Permite conocer la cantidad de solicitudes pendientes y totales 
        del docente. */
        axios
          .get(`http://localhost:8000/solicitudesDocente/${idDocente}`)
          .then(function (responseTwo) {
            let solicitudes = responseTwo.data;
            // Obtención núm. de solicitudes totales.
            that.solicitudesTotales = solicitudes.length;

            // Obtención núm. de solicitudes pendientes.
            for (var i = 0; i < solicitudes.length; i++) {
              if (solicitudes[i].estado == "P") {
                that.solicitudesPendientes++;
              }
            }
          });

        /* Permite conocer las evaluaciones que no han sido calificadas y 
        están fuera de plazo de entrega */
        axios
          .get(`http://localhost:8000/get/evPendientesEntrega/${idDocente}`)
          .then(function (responseThree) {
            that.evPendientesEntrega = responseThree.data;
            for (var i = 0; i < responseThree.data.length; i++) {
              if (
                moment().startOf("day") >
                moment(responseThree.data[i].fechaEntrega)
              ) {
                that.evFueraEntrega.push(responseThree[i]);
              }
            }
          });
      });
    /* Permite conocer la cantidad de coordinaciones inscritas por el 
      docente, y además, las que son de teoría y laboratorio */
    axios
      .get(`http://localhost:8000/cursosDocente/${identificacionUsuario}`)
      .then(function (response) {
        that.coordinacionesTotales = response.data.length;
        for (var i = 0; i < response.data.length; i++) {
          if (
            response.data[i].id_coordinacion.id_asignatura.componente === "T"
          ) {
            that.coordinacionesTeoria++;
          } else {
            that.coordinacionesLaboratorio++;
          }
        }
      });
  },
  methods: {
    solicitudes() {
      this.$router.push({ name: "Apelacionesdocente" });
    },

    coordinaciones() {
      this.$router.push({ name: "cursosDocente" });
    },

    ingresarEvaluacion(index) {
      let idDocente = this.evPendientesEntrega[index].id_docente.id;
      let bloqueHorario =
        this.evPendientesEntrega[index].id_coordinacion.bloques_horario;
      let nombreEvaluacion = this.evPendientesEntrega[index].nombre;
      this.$router.push({
        path: `/docente/${idDocente}/curso/${bloqueHorario}/add/calificacion/${nombreEvaluacion}`,
      });
    },
  },
};
</script>

<style></style>
