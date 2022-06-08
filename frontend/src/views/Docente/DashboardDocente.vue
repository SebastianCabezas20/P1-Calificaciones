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
        <div class="col-md-3 cuadradoDashboard" @click="solicitudes()">
          <!-- Icono -->
          <div class="iconoDashboard">
            <span class="fa-solid fa-file-circle-exclamation fa-3x"></span>
          </div>
          <!-- Texto -->
          <h2>Solicitudes de revisión pendientes</h2>
          <!-- Dato -->
          <h3>{{ solicitudesPendientes }} - {{ solicitudesTotales }}</h3>
        </div>
        <div class="col-md"></div>
      </div>

      <div class="row" style="background-color: #ffffff">
        <div class="col-md rectanguloDashboard">
          <h2>Próximas entregas de calificaciones</h2>
          <table class="tableDashboard">
            <thead>
              <tr>
                <th style="width: 10%">Código</th>
                <th style="width: 40%">Asignatura</th>
                <th>Evaluación</th>
                <th>Entrega de notas</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(evaluacion, index) in evPendientesEntrega.slice(0, 3)"
                :key="index"
                @click="evaluacionPendiente(index)"
              >
                <td>
                  {{ evaluacion.id_coordinacion.id_asignatura.codigo }}-{{
                    evaluacion.id_coordinacion.coordinacion
                  }}-{{ evaluacion.id_coordinacion.seccion }}
                </td>
                <td>{{ evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
                <td>{{ evaluacion.nombre }}</td>
                <td>{{ evaluacion.fechaEntrega }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col-md-3"></div>
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
      solicitudesPendientes: 0,
      solicitudesTotales: 0,
      evPendientesEntrega: [],
    };
  },
  mounted() {
    let identificacionUsuario = this.$store.getters.idUsuario;
    let that = this;
    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        let idDocente = response.data.id;
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
        axios
          .get(`http://localhost:8000/get/evPendientesEntrega/${idDocente}`)
          .then(function (responseThree) {
            that.evPendientesEntrega = responseThree.data;
            console.log(responseThree.data);
          });
      });
  },
  methods: {
    solicitudes() {
      this.$router.push({ name: "Apelacionesdocente" });
    },
    evaluacionPendiente(index) {
      let idCurso = this.evPendientesEntrega[index].id_coordinacion.id;
      let idEvaluacion = this.evPendientesEntrega[index].id;
      this.$router.push({ path: `/docente/curso/${idCurso}/add/calificacion/${idEvaluacion}` });
    }
  },
};
</script>

<style></style>
