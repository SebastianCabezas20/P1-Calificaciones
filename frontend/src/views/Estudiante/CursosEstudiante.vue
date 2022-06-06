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
        <h1 class="textTitleV2">Mis Cursos Inscritos</h1>
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
          <template v-for="asignatura in asignaturas" :key="asignatura.id">
            <tr>
              <td>
                {{ asignatura.id_coordinacion.id_asignatura.codigo }}-{{
                  asignatura.id_coordinacion.coordinacion
                }}-{{ asignatura.id_coordinacion.seccion }}
              </td>
              <td>{{ asignatura.id_coordinacion.id_asignatura.nombre }}</td>
              <td>{{ asignatura.id_coordinacion.bloques_horario }}</td>
              <td>{{ asignatura.id_coordinacion.id_asignatura.nivel }}</td>
              <td>
                <button
                  type="button"
                  class="botonTabla"
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
    console.log(identificacionUsuario);
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

<style></style>
