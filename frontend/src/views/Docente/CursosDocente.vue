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
        <h3 class="textTitleV2">Mis coordinaciones (Teoría)</h3>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th class="row-Codigo">Código</th>
            <th class="row-Nombre">Nombre</th>
            <th class="row-Horario">Horario</th>
            <th class="row-Nivel">Nivel</th>
            <th class="row-ButtonText"></th>
          </tr>
        </thead>
        <tbody>
          <template
            v-for="coordinacion in coordinaciones"
            :key="coordinacion.id"
          >
            <tr
              v-if="
                coordinacion.id_coordinacion.id_asignatura.componente === 'T'
              "
            >
              <td>
                {{ coordinacion.id_coordinacion.id_asignatura.codigo }}-{{
                  coordinacion.id_coordinacion.coordinacion
                }}-{{ coordinacion.id_coordinacion.seccion }}
              </td>
              <td>{{ coordinacion.id_coordinacion.id_asignatura.nombre }}</td>
              <td>{{ coordinacion.id_coordinacion.bloques_horario }}</td>
              <td>{{ coordinacion.id_coordinacion.id_asignatura.nivel }}</td>
              <td>
                <button
                  @click="
                    getAsignatura($event, coordinacion.id_coordinacion.bloques_horario)
                  "
                  type="button"
                  class="botonTabla"
                >
                  Más Información
                </button>
              </td>
            </tr>
          </template>
        </tbody>
      </table>

      <div class="titleSectionV2">
        <h3 class="textTitleV2">Mis coordinaciones (Laboratorio)</h3>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th class="row-Codigo">Código</th>
            <th class="row-Nombre">Nombre</th>
            <th class="row-Horario">Horario</th>
            <th class="row-Nivel">Nivel</th>
            <th class="row-ButtonText"></th>
          </tr>
        </thead>
        <tbody>
          <template
            v-for="coordinacion in coordinaciones"
            :key="coordinacion.id"
          >
            <tr
              v-if="
                coordinacion.id_coordinacion.id_asignatura.componente === 'L'
              "
            >
              <td>
                {{ coordinacion.id_coordinacion.id_asignatura.codigo }}-{{
                  coordinacion.id_coordinacion.coordinacion
                }}-{{ coordinacion.id_coordinacion.seccion }}
              </td>
              <td>{{ coordinacion.id_coordinacion.id_asignatura.nombre }}</td>
              <td>{{ coordinacion.id_coordinacion.bloques_horario }}</td>
              <td>{{ coordinacion.id_coordinacion.id_asignatura.nivel }}</td>
              <td>
                <button
                  v-on:click="
                    getAsignatura($event, coordinacion.id_coordinacion.bloques_horario)
                  "
                  type="button"
                  class="botonTabla"
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
    getAsignatura: function (event, bloqueHorario) {
      // Pasar una variable de una vista a otra. En este caso para obtener los cursos espejos, se pasa el horario
      // para asi tener los cursos que tienen el horario en comun de un usuario
      this.$router.push({ path: `/docente/curso/${bloqueHorario}` }); 
    },

  },
};
</script>

<style></style>
