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
        <h3 class="textTitleV2">Solicitudes de Apelación</h3>
      </div>
      <table class="tableV2">
        <thead>
          <tr>
            <th>Nombre asignatura</th>
            <th>Estudiante</th>
            <th>Evaluacion</th>
            <th>Fecha de envío</th>
            <th>Estado</th>
            <th class="row-ButtonText"></th>
          </tr>
        </thead>
        <tbody>
          <template v-for="solicitud in solicitudes" :key="solicitud.id">
            <tr>
              <SolicitudesDocente
                :solicitud_revision="solicitud"
                @EventIdEvaluacion="
                  (idEstudiante, idEvaluacion) =>
                    ingresar(idEstudiante, idEvaluacion)
                "
              />
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import SolicitudesDocente from "../../components/SolicitudesDocente.vue";
import axios from "axios";
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
    SolicitudesDocente,
  },
  data() {
    return {
      solicitudes: [],
    };
  },
  mounted() {
    let identificacionUsuario = this.$store.getters.idUsuario;
    let ins = this;
    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        let idDocente = response.data.id;
        axios
          .get(`http://localhost:8000/solicitudesDocente/${idDocente}`)
          .then(function (responseTwo) {
            ins.solicitudes = responseTwo.data;
          });
      });
  },
  methods: {
    // Para conectar se necesita idEstudiante y idEvaluacion de esa apelacion
    ingresar(idEst, idEval) {
      router.push(`/docente/apelacion/answer/${idEst}/${idEval}`);
    },
  },
};
</script>

<style></style>
