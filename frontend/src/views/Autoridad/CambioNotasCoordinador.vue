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
        <h4 class="textTitleV2">Modificaciones de calificaciones</h4>
      </div>
      <!--Filtros-->
      <div class="row" style="background-color: #ffffff">
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Evaluación</span>
            <input
              type="text"
              class="form-control"
              v-model="evaluacionFiltro"
              placeholder="Evaluación a buscar"
            />
            <span class="input-group-text mt-4">Docente</span>
            <input
              type="text"
              class="form-control"
              v-model="docenteFiltro"
              placeholder="Docente a buscar"
            />
          </div>
        </div>

        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Estudiante</span>
            <input
              type="text"
              class="form-control"
              v-model="estudianteFiltro"
              placeholder="Estudiante a buscar"
            />
          </div>
        </div>
      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th style="width: 10%;" >Evaluación</th>
            <th style="width: 20%;">Asignatura</th>
            <th>Estudiante</th>
            <th>Docente</th>
            <th>Fecha de modificación</th>
            <th>Nota anterior</th>
            <th>Nota nueva</th>
            <th>Motivo</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="cambio_nota in cambio_notas" :key="cambio_nota.id">
            <tr
              v-show="
                filterEvaluacion(
                  cambio_nota.id_calificacion.id_evaluacion.nombre
                ) &&
                filterDocente(
                  cambio_nota.id_calificacion.id_evaluacion.id_docente
                    .id_usuario.first_name,
                  cambio_nota.id_calificacion.id_evaluacion.id_docente
                    .id_usuario.last_name
                ) &&
                filterEstudiante(
                  cambio_nota.id_calificacion.id_estudiante.id_usuario
                    .first_name,
                  cambio_nota.id_calificacion.id_estudiante.id_usuario.last_name
                )
              "
            >
              <td>
                {{ cambio_nota.id_calificacion.id_evaluacion.nombre }}
              </td>
              <td>
                {{
                  cambio_nota.id_calificacion.id_evaluacion.id_coordinacion
                    .id_asignatura.nombre
                }}
              </td>
              <td>
                {{
                  cambio_nota.id_calificacion.id_estudiante.id_usuario
                    .first_name
                }}
                {{
                  cambio_nota.id_calificacion.id_estudiante.id_usuario.last_name
                }}
              </td>
              <td>
                {{
                  cambio_nota.id_calificacion.id_evaluacion.id_docente
                    .id_usuario.first_name
                }}
                {{
                  cambio_nota.id_calificacion.id_evaluacion.id_docente
                    .id_usuario.last_name
                }}
              </td>
              <td>{{ cambio_nota.fecha_cambio }}</td>
              <td>{{ cambio_nota.anterior_nota }}</td>
              <td>{{ cambio_nota.actual_nota }}</td>
              <td>{{ cambio_nota.motivo }}</td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import ApelacionesCoordinador from "../../components/ApelacionesCoordinador.vue";
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
    ApelacionesCoordinador,
  },
  props: ["idCurso"],
  data() {
    return {
      cambio_notas: [],
      estudianteFiltro: "",
      evaluacionFiltro: "",
      docenteFiltro: "",
    };
  },
  created() {
    let ins = this;
    let IDcurso = this.idCurso;
    axios
      .get(`http://localhost:8000/get/cambio/calificacion/curso/${IDcurso}`)
      .then(function (response) {
        ins.cambio_notas = response.data;
      });
  },
  methods: {
    filterEvaluacion(evaluacion) {
      let n = Array(evaluacion);
      return n[0].toLocaleLowerCase().indexOf(this.evaluacionFiltro) >= 0;
    },
    filterDocente(nombre, apellido) {
      let n = Array(nombre + " " + apellido);
      return n[0].indexOf(this.docenteFiltro) >= 0;
    },
    filterEstudiante(nombre, apellido) {
      let n = Array(nombre + " " + apellido);
      return n[0].indexOf(this.estudianteFiltro) >= 0;
    },
  },
};
</script>

<style></style>
