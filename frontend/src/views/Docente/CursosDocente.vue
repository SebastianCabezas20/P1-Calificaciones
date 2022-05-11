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
        <h3 class="textTitle">Docencia: Mis Coordinaciones (Teoría)</h3>
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
            <template v-for="coordinacion in coordinaciones" :key="coordinacion.id">
              <tr
                v-if="
                  coordinacion.id_coordinacion.id_asignatura.componente === 'T'
                "
              >
                <td>{{ coordinacion.id_coordinacion.id_asignatura.codigo }}</td>
                <td>{{ coordinacion.id_coordinacion.id_asignatura.nombre }}</td>
                <td>{{ coordinacion.id_coordinacion.bloques_horario }}</td>
                <td>
                  {{ coordinacion.id_coordinacion.id_asignatura.componente }}
                </td>
                <td>{{ coordinacion.id_coordinacion.id_asignatura.nivel }}</td>
                <td>
                  <button
                    @click="getAsignatura($event, coordinacion.id_coordinacion.id)"
                    type="button"
                    class="btn btn-light"
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

  <div class="contentViews">
    <div class="centralContent">
      <div class="titleSection">
        <h3 class="textTitle">Docencia: Mis Coordinaciones (Laboratorio)</h3>
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
            <template v-for="coordinacion in coordinaciones" :key="coordinacion.id">
              <tr
                v-if="
                  coordinacion.id_coordinacion.id_asignatura.componente === 'L'
                "
              >
                <td>{{ coordinacion.id_coordinacion.id_asignatura.codigo }}</td>
                <td>{{ coordinacion.id_coordinacion.id_asignatura.nombre }}</td>
                <td>{{ coordinacion.id_coordinacion.bloques_horario }}</td>
                <td>
                  {{ coordinacion.id_coordinacion.id_asignatura.componente }}
                </td>
                <td>{{ coordinacion.id_coordinacion.id_asignatura.nivel }}</td>
                <td>
                  <button
                    v-on:click="getAsignatura($event, coordinacion.id_coordinacion.id)"
                    type="button"
                    class="btn btn-light"
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
      coordinaciones: [],
    };
  },
  mounted() {
    let ins = this;
    let idUsuarioLogeado = this.$store.getters.idUsuario;
    axios
      .get(`http://localhost:8000/cursosDocente/${idUsuarioLogeado}`)
      .then(function (response) {
        ins.coordinaciones = response.data;
      });
  },
  methods: {
    getAsignatura: function (event, idCoordinacion) {
      // Pasar una variable de una vista a otra.
      this.$router.push({ path: `/docente/curso/${idCoordinacion}` });
    },
  },
};
</script>

<style></style>
