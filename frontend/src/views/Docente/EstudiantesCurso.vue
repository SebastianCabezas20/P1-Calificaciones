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
        <h3 class="textTitleV2">Estudiantes inscritos</h3>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th style="width: 40%">Estudiante</th>
            <th style="width: 40%">Rut</th>
            <th style="width: 20%"></th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(estudiante, index) in estudiantesInscritos">
            <tr>
              <td>
                {{ estudiante.id_estudiante.id_usuario.first_name }}
                {{ estudiante.id_estudiante.id_usuario.last_name }}
              </td>
              <td>
                {{ estudiante.id_estudiante.rut }}-{{
                  estudiante.id_estudiante.dig_verificador
                }}
              </td>
              <td>
                <div class="text-center">
                  <button
                    class="fa-solid fa-plus botonTabla"
                    type="button"
                    v-on:click="verLaboratorio($event, index)"
                  ></button>
                </div>
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
import SolicitudesDocente from "../../components/SolicitudesDocente.vue";
import axios from "axios";
import router from "../../router";

export default {
  props: ["idCurso", "idDocente"],
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      estudiantesInscritos: [],
    };
  },
  mounted() {
    /* idCurso corresponde al bloque horario. */
    let identificacionCurso = this.idCurso;
    let identificacionDocente = this.idDocente;
    let ins = this;
    axios
      .get(
        `http://localhost:8000/calificacion/coordinacion/${identificacionCurso}/${identificacionDocente}/CE`
      )
      .then(function (response) {
        ins.estudiantesInscritos = response.data;
      });
  },
  methods: {
    verLaboratorio: function (event, index) {
      let idEstudiante = this.estudiantesInscritos[index].id_estudiante.id;
      let that = this;
      
      // Caso 1: El listado de estudiantes mostrado es de Teoría.
      if (
        this.estudiantesInscritos[index].id_coordinacion.id_asignatura
          .componente === "T"
      ) {
        axios
          .get(
            `http://localhost:8000/isEstudianteInscrito/${this.idCurso}/${this.idDocente}/L/${idEstudiante}`
          )
          .then(function (response) {
            if (response.data === false) {
              that.$swal.fire({
                icon: "error",
                title: "Estudiante no inscrito en Laboratorio",
                text: "El estudiante cursa únicamente el componente teoría de esta asignatura",
              });
              return;
            }

            /* Variables a necesitar para el ruteo. */
            let codigoAsig = response.data[0].id_coordinacion.id_asignatura.codigo;
            let idUsuario = response.data[0].id_estudiante.id;
            that.$router.push({
              path: `/docente/asignatura/${codigoAsig}/L/estudiante/${idUsuario}`,
            });
          });
      }
      // Caso 2: El listado de estudiantes mostrado es de Laboratorio.
      else {
        axios
          .get(
            `http://localhost:8000/isEstudianteInscrito/${this.idCurso}/${this.idDocente}/T/${idEstudiante}`
          )
          .then(function (response) {
            if (response.data === false) {
              that.$swal.fire({
                icon: "error",
                title: "Estudiante no inscrito en Teoria",
                text: "El estudiante cursa únicamente el componente laboratorio de esta asignatura",
              });
              return;
            }

            /* Variables a necesitar para el ruteo. */
            let codigoAsig = response.data[0].id_coordinacion.id_asignatura.codigo;
            let idUsuario = response.data[0].id_estudiante.id;
            that.$router.push({
              path: `/docente/asignatura/${codigoAsig}/T/estudiante/${idUsuario}`,
            });
          });
      }
    },
  },
};
</script>

<style></style>
