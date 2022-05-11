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
        <h3 class="textTitle">
          Modificacion de Calificaciones: -nombre Curso-
        </h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Rut</th>
              <th>Nombre</th>
              <th>Evaluación</th>
              <th>Nota Actual</th>
              <th>Fecha</th>
              <th>Nueva Calificación</th>
              <th>Observacion</th>
            </tr>
          </thead>
          <tbody>
            <tr scope="row" v-for="calificacion in calificaciones" :key="calificacion.id">
              <CalificacionModify :calificacion="calificacion" />
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import CalificacionModify from "../../components/CalificacionModify.vue";
import axios from "axios";

export default {
  components: {
    Sidebar,
    Navbar,
    CalificacionModify,
  },
  data() {
    return {
      calificaciones: [],
    };
  },
  mounted() {
    let ins = this;
    axios.get("http://localhost:8000/getCalificacionesPerAsignaturaEvaluacion").then(function (response) {
      console.log(response.data);
      ins.calificaciones = response.data;
    });
  },
};
</script>

<style>
.centralContent {
  margin: auto;
  width: 98%;
  margin-top: 10px;
  font-family: "Inter", sans-serif;
}

.titleSection {
  display: block;
  background: #c4c4c4;
  border: 2px solid #004883;
  border-radius: 20px;
  padding: 3px;
  margin-bottom: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.textTitle {
  text-align: center;
  font-size: 30px;
  color: #000;
  font-weight: 600;
}

.tableContent {
  background: #c4c4c4;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  border: 2px solid #004883;
  overflow-y: auto;
  overflow-x: hidden;
  margin-bottom: 20px;
}

.tableContent .table {
  border-collapse: collapse;
}

.tableContent .table thead tr {
  text-align: center;
}

.tableContent .table thead tr th {
  padding: 8px;
}
</style>
