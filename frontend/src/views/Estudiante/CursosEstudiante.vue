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
        <h1 class="textTitleV2">Cursos inscritos</h1>
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
                {{ asignatura.id_coordinacion.id_asignatura.codigo }}
              </td>
              <td>{{ asignatura.id_coordinacion.id_asignatura.nombre }}</td>
              <td>{{ asignatura.id_coordinacion.bloques_horario }}</td>
              <td>{{ asignatura.id_coordinacion.id_asignatura.nivel }}</td>
              <td>
                <span 
                  class="p-3"
                  title="Calificaciones ingresadas los últimos tres días."
                >
                {{novedadesCurso(asignatura)}}
                </span>
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
import moment from 'moment';

export default {
  components: {
    Sidebar,
    Navbar,
    Asignatura,
  },
  data() {
    return {
      asignaturas: [],
      calificacionesEstudiante: [],
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

    axios
      .get(`http://localhost:8000/get/calificaciones/estudiante/${identificacionUsuario}`)
      .then(function (response) {
        ins.calificacionesEstudiante = response.data;
      });
  },
  methods: {
    ingresar(codigo) {
      router.push(`/estudiante/calificaciones/${codigo}`);
    },

    /* Se cuentan las calificaciones calificadas en los últimos tres días,
    con el fin de indicarlas en la vista.  */
    novedadesCurso(asignatura) {
      let idCurso = asignatura.id_coordinacion.id_asignatura.id;
      let fechaActual = moment().startOf('day');
      let calificacionesNuevas = 0;
      
      for(var i = 0; i < this.calificacionesEstudiante.length; i++){
        if(this.calificacionesEstudiante[i].id_evaluacion.id_coordinacion.id_asignatura.id == idCurso){
          if(moment.duration(fechaActual.diff(this.calificacionesEstudiante[i].fecha_entrega)).asDays() <= 3){
            calificacionesNuevas++;
          }
        }
      }
      return calificacionesNuevas;
    },
  },
};
</script>

<style></style>
