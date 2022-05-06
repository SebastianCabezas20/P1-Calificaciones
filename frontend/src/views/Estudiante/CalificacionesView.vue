<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      
      <div>
        <InformacionCurso />
      </div>

      <div class="componentCourse">
        <div class="titleSection">
          <h3 class="textTitle">Calificaciones Catedra</h3>
        </div>

        <div class="tableContent">
          <table class="table">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Observacion</th>
                <th>Calificacion</th>
                <th>Ponderacion</th>
                <th>Estado</th>
                <th>Fecha</th>
                <th>Apelar</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="calificacion in calificaciones" :key="calificacion.id">
                <CalificacionInfo :calificacion="calificacion" />
              </tr>
            </tbody>
          </table>
        </div>

        <div class="stateStudent">
          <h4>Estado del estudiante</h4>
        </div>
      </div>

      <div class="componentCourse">
        <div class="titleSection">
          <h3 class="textTitle">Calificaciones laboratorio</h3>
        </div>

        <div class="tableContent">
          <table class="table">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Observacion</th>
                <th>Calificacion</th>
                <th>Ponderacion</th>
                <th>Estado</th>
                <th>Fecha</th>
                <th>Apelar</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="calificacion in calificaciones" :key="calificacion.id">
                <CalificacionInfo :calificacion="calificacion" />
              </tr>
            </tbody>
          </table>
        </div>

        <div class="stateStudent">
          <h4>Estado del estudiante</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";
import axios from "axios";

export default {
  data() {
    return {
      calificaciones: [],
    };
  },
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
  mounted() {
    let ins = this;
    axios.get("http://localhost:8000/calificaciones").then(function (response) {
      console.log(response.data);
      ins.calificaciones = response.data;
    });
  },
};
</script>

<style>
.componentCourse {
  margin-bottom: 30px;
}

.stateStudent {
  background-color: #eeeeee;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  padding: 10px;
}
</style>
