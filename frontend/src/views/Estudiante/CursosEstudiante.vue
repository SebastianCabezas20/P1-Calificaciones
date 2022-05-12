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
        <h1 class="textTitle">Mis Cursos Inscritos</h1>
      </div>

      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Código</th>
              <th scope="col">Nombre</th>
              <th scope="col">Horario</th>
              <th scope="col">Componente</th>
              <th scope="col">Nivel</th>
              <th scope="col">Detalles</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="asignatura in asignaturas" :key="asignatura.id">
              <tr scope="row">
                <td>{{ asignatura.id_coordinacion.id_asignatura.codigo }}</td>
                <td>{{ asignatura.id_coordinacion.id_asignatura.nombre }}</td>
                <td>{{ asignatura.id_coordinacion.bloques_horario }}</td>
                <td>
                  {{ asignatura.id_coordinacion.id_asignatura.componente }}
                </td>
                <td>{{ asignatura.id_coordinacion.id_asignatura.nivel }}</td>
                <td>
                  <button
                    type="button"
                    class="btn btn-light"
                    v-on:click="
                      ingresar(asignatura.id_coordinacion.id_asignatura.codigo)
                    "
                  >
                    Más Información
                  </button>
                </td>
              </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import Asignatura from "../../components/Asignatura.vue";
import axios from "axios";
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
    Asignatura,
  },
  data() {
    return {
      asignaturas: [],
    };
  },
  mounted() {
    let identificacionUsuario = this.$store.getters.idUsuario;
    let ins = this;
    axios
      .get(`http://localhost:8000/cursosEstudiante/${identificacionUsuario}`)
      .then(function (response) {
        ins.asignaturas = response.data;
      });
  },
  methods: {
    ingresar(codigo) {
      router.push(`/estudiante/calificaciones/${codigo}`);
    },
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
