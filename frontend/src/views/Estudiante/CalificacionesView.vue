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
        <h3 class="textTitleV2">Teoría</h3>
      </div>

      <div
        class="row"
        style="margin: 0px 2px 20px 2px; padding: 10px 0px; background-color: #fff"
      >
        <div class="col-sm" style="margin: 0px; padding: 0px">
          <p class="informationCalification">
            Asignatura:
            {{ informacionTeoria[0].id_coordinacion.id_asignatura.nombre }}
          </p>
          <p class="informationCalification">
            Nivel:
            {{ informacionTeoria[0].id_coordinacion.id_asignatura.nivel }}
          </p>
        </div>

        <div class="col-sm">
          <div
            class="col-sm"
            v-for="(info, id) in informacionTeoria"
            :key="info.id"
          >
            <label v-if="id == 0" class="informationCalification"
              >Docente: {{ info.id_docente.id_usuario.first_name }}
              {{ info.id_docente.id_usuario.last_name }}</label
            >
            <label
              v-else
              style="margin-left: 79px"
              class="informationCalification"
              >{{ info.id_docente.id_usuario.first_name }}
              {{ info.id_docente.id_usuario.last_name }}</label
            >
          </div>
        </div>
      </div>

      <div class="componentCourse">
        <div class="titleSectionV2">
          <h3 class="textSubTitleV2">Evaluaciones calificadas</h3>
        </div>

        <table class="tableV2">
          <thead>
            <tr>
              <th style="width: 25%">Evaluación</th>
              <th style="width: 25%">Obervaciones</th>
              <th style="width: 10%">Calificación</th>
              <th style="width: 10%">Pondera</th>
              <th style="width: 20%">Fecha de entrega</th>
              <th style="width: 10%"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="calificacion in calificacionesTeoria"
              :key="calificacion.id"
            >
              <CalificacionInfo
                :calificacion="calificacion"
                @EventBoton="(id) => ingresar(id)"
                :CalificacionSolicitudes="
                  this.idsCalificacionesSolicitudesTeoria
                "
              />
            </tr>
          </tbody>
        </table>

        <div class="titleSectionV2">
          <h3 class="textSubTitleV2">Evaluaciones pendientes</h3>
        </div>

        <table class="tableV2">
          <thead>
            <tr>
              <th>Evaluación</th>
              <th>Pondera</th>
              <th>Fecha de evaluación</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="evaluacion in evaluacionesSinNotaTeoria"
              :key="evaluacion.id"
            >
              <td>{{ evaluacion.nombre }}</td>
              <td>{{ evaluacion.ponderacion * 100 }}%</td>
              <td>{{ evaluacion.fechaEvActual }}</td>
            </tr>
          </tbody>
        </table>

        <!-- Comentado, ya que no está claro que vamos a gregar aquí. -->
        <!-- <div class="stateStudent">
          <h4>Estado del estudiante</h4>
        </div> -->
      </div>

      <div class="lineaSeparatoria"></div>

      <div v-if="this.mostrar">
        <div class="titleSectionV2">
          <h3 class="textTitleV2">Laboratorio</h3>
        </div>

        <div
          class="row"
          style="margin: 0px 2px 20px 2px; padding: 10px 0px; background-color: #fff"
        >
          <div class="col-sm" style="margin: 0px; padding: 0px">
            <p class="informationCalification">
              Asignatura:
              {{
                informacionLaboratorio[0].id_coordinacion.id_asignatura.nombre
              }}
            </p>
            <p class="informationCalification">
              Nivel:
              {{
                informacionLaboratorio[0].id_coordinacion.id_asignatura.nivel
              }}
            </p>
          </div>
          <div class="col">
            <div
              class="col"
              v-for="(info, id) in informacionLaboratorio"
              :key="info.id"
            >
              <label v-if="id == 0" class="informationCalification"
                >Docente: {{ info.id_docente.id_usuario.first_name }}
                {{ info.id_docente.id_usuario.last_name }}</label
              >
              <label
                v-else
                style="margin-left: 79px"
                class="informationCalification"
                >{{ info.id_docente.id_usuario.first_name }}
                {{ info.id_docente.id_usuario.last_name }}</label
              >
            </div>
          </div>
        </div>

        <div class="componentCourse">
          <div class="titleSectionV2">
            <h3 class="textSubTitleV2">Evaluaciones calificadas</h3>
          </div>
          <table class="tableV2">
            <thead>
              <tr>
                <th style="width: 25%">Evaluación</th>
                <th style="width: 25%">Obervaciones</th>
                <th style="width: 10%">Calificación</th>
                <th style="width: 10%">Pondera</th>
                <th style="width: 20%">Fecha de entrega</th>
                <th style="width: 10%"></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="calificacion in calificacionesLaboratorio"
                :key="calificacion.id"
              >
                <CalificacionInfo
                  :calificacion="calificacion"
                  @EventBoton="(id) => ingresar(id)"
                  :CalificacionSolicitudes="
                    this.idsCalificacionesSolicitudesLab
                  "
                />
              </tr>
            </tbody>
          </table>

          <div class="titleSectionV2">
            <h3 class="textSubTitleV2">Evaluaciones pendientes</h3>
          </div>

          <table class="tableV2">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Ponderacion</th>
                <th>Fecha de evaluación</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="evaluacion in evaluacionesSinNotaLaboratorio"
                :key="evaluacion.id"
              >
              <td>{{ evaluacion.nombre }}</td>
              <td>{{ evaluacion.ponderacion * 100 }}%</td>
              <td>{{ evaluacion.fechaEvActual }}</td>
              </tr>
            </tbody>
          </table>

          <!-- <div class="stateStudent">
            <h4>Estado del estudiante</h4>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";
import axios from "axios";
import router from "../../router";

export default {
  data() {
    return {
      calificacionesTeoria: [],
      evaluacionesSinNotaTeoria: [],
      informacionTeoria: [],
      calificacionesLaboratorio: [],
      evaluacionesSinNotaLaboratorio: [],
      informacionLaboratorio: [],
      mostrar: false,
      idsCalificacionesSolicitudesTeoria: [],
      idsCalificacionesSolicitudesLab: [],
    };
  },
  props: ["codigoAsignatura"],
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
  created() {
    let ins = this;
    let codigoAsig = this.codigoAsignatura;
    const idUsuario = this.$store.getters.idUsuario;
    console.log(
      "ID del usuario:" + idUsuario + "ID de la asignatura:" + codigoAsig
    );

    axios
      .get(
        `http://localhost:8000/calificacionesTeoria/${codigoAsig}/${idUsuario}`
      )
      .then(function (response) {
        ins.calificacionesTeoria = response.data[0];
        ins.evaluacionesSinNotaTeoria = response.data[1];
        ins.idsCalificacionesSolicitudesTeoria = response.data[2];
      });
    axios
      .get(
        `http://localhost:8000/calificacionesLaboratorio/${codigoAsig}/${idUsuario}`
      )
      .then(function (response) {
        if (response.data[0].length != 0) {
          console.log(response.data.length);
          ins.calificacionesLaboratorio = response.data[0];
          ins.evaluacionesSinNotaLaboratorio = response.data[1];
          ins.idsCalificacionesSolicitudesLab = response.data[2];
          ins.mostrar = true;
        }
      });
    axios
      .get(`http://localhost:8000/InformacionTeoria/${codigoAsig}`)
      .then(function (response) {
        ins.informacionTeoria = response.data;
      });
    axios
      .get(`http://localhost:8000/InformacionLaboratorio/${codigoAsig}`)
      .then(function (response) {
        if (response.data.length != 0) {
          ins.informacionLaboratorio = response.data;
          ins.mostrar = true;
        }
      });
  },
  methods: {
    ingresar(idCalificacion) {
      router.push(`/estudiante/add/solicitud/${idCalificacion}`);
    },
  },
};
</script>

<style>
.componentCourse {
  margin-bottom: 30px;
}

.stateStudent {
  background-color: #eeeeee;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  padding: 10px;
}
</style>
