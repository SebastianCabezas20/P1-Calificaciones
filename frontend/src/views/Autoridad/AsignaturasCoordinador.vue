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
          Cursos Coordinador
        </h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Codigo</th>
              <th>Curso</th>
              <th>Componente</th>
              <th>Accion</th>
            </tr>
          </thead>
          <tbody>
            <tr scope="row" v-for="asignatura in asignaturas" :key="asignatura.id">
              <AsignaturasCoordinador :asignatura="asignatura" />
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
import AsignaturasCoordinador from "../../components/AsignaturasCoordinador.vue";
import axios from "axios";

export default {
  components: {
    Sidebar,
    Navbar,
    AsignaturasCoordinador,
  },
  data() {
    return {
      asignaturas: [],
      idCoordinador:0,
    };
  },
  mounted() {
    // Forma de capturar el id del Jefe de Carrera, dado el id del usuario que inició sesión.
    const that = this;
    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/api/coordinador/${identificacionUsuario}`)
      .then(function (response) {
        that.idCoordinador = response.data.id;
      });
    let idCoor = this.idCoordinador;
    axios.get(`http://localhost:8000/asignaturascoordinador/${idCoor}`).then(function (response) {
      console.log(response.data);
      that.asignaturas = response.data;
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
