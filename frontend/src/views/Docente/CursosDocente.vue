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
        <h3 class="textTitle">Docencia: Mis Asignaturas (Teoría)</h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Código</th>
              <th>Nombre</th>
              <th>Nivel</th>
              <th>Componente</th>
              <th>Calificaciones</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="asignatura in asignaturas" :key="asignatura.id">
              <tr v-if="asignatura.id_coordinacion.id_asignatura.componente === 'T'">
                <Asignatura :asignatura="asignatura" />
              </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSection">
        <h3 class="textTitle">Docencia: Mis Asignaturas (Laboratorio)</h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Código</th>
              <th>Nombre</th>
              <th>Nivel</th>
              <th>Componente</th>
              <th>Calificaciones</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="asignatura in asignaturas" :key="asignatura.id">
              <tr v-if="asignatura.id_coordinacion.id_asignatura.componente === 'L'">
                <Asignatura :asignatura="asignatura" />
              </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import Asignatura from "../../components/Asignatura.vue";
import axios from "axios";
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
    let ins = this;
    axios.get("http://localhost:8000/cursosDocente").then(function (response) {
      console.log(response.data);
      ins.asignaturas = response.data;
    });
  },
};
</script>

<style></style>
