<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div
        id="filaInformacion"
        class="row row-cols-3"
      >
        <div class="col">
          {{ informacionTeoria[0].id_coordinacion.id_asignatura.nombre }}
        </div>
        <div class="col">
          Nivel: {{ informacionTeoria[0].id_coordinacion.id_asignatura.nivel }}
        </div>
        <div class="col">
          <div class="col" v-for="(info,id) in informacionTeoria" :key="info.id">
          <label v-if="id == 0">Docente: {{info.id_docente.id_usuario.username}}</label>
          <label v-else style="margin-left:72px">{{info.id_docente.id_usuario.username}}</label>
          </div>
        </div>
      </div>

      <div class="componentCourse">
        <div class="titleSection">
          <h3 class="textTitle">Calificaciones Catedra</h3>
        </div>

        <div class="tableContent">
          <table class="table text-center">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Observacion</th>
                <th>Calificacion</th>
                <th>Ponderacion</th>
                <th>Fecha entrega</th>
                <th>Apelar</th>
                <!--Saque estado de la evaluacion-->
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
                />
              </tr>
            </tbody>
          </table>
        </div>

        <div class="row">
          <div class="col-md-3">
            Evaluaciones pendientes
          </div>
        </div>
        <div class="tableContent">
          <table class="table text-center">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Ponderacion</th>
                <th>Fecha de evaluación</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="evaluacion in evaluacionesSinNotaTeoria" :key="evaluacion.id">
                <td>{{evaluacion.nombre}}</td>
                <td>{{evaluacion.ponderacion}}</td>
                <td>{{evaluacion.fechaEvActual}}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="stateStudent">
          <h4>Estado del estudiante</h4>
        </div>
      </div>
      <br><br><br>

       <div
        v-if="this.mostrar"
        id="filaInformacion"
        class="row row-cols-3"
      >
        <div class="col">
          {{ informacionLaboratorio[0].id_coordinacion.id_asignatura.nombre }}
        </div>
        <div class="col">
          Nivel: {{ informacionLaboratorio[0].id_coordinacion.id_asignatura.nivel }}
        </div>
        <div class="col">
          <div class="col" v-for="(info,id) in informacionLaboratorio" :key="info.id">
          <label v-if="id == 0">Docente: {{info.id_docente.id_usuario.username}}</label>
          <label v-else style="margin-left:72px">{{info.id_docente.id_usuario.username}}</label>
          </div>
        </div>
      </div>
      
      
      <div v-if="this.mostrar" class="componentCourse">
        <div class="titleSection">
          <h3 class="textTitle">Calificaciones laboratorio</h3>
        </div>

        <div class="tableContent">
          <table class="table text-center">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Observacion</th>
                <th>Calificacion</th>
                <th>Ponderacion</th>
                <th>Fecha entrega</th>
                <th>Apelar</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="calificacion in calificacionesLaboratorio"
                :key="calificacion.id"
              >
                <CalificacionInfo :calificacion="calificacion" />
              </tr>
            </tbody>
          </table>
        </div>
        <div class="row">
          <div class="col-md-3">
            Evaluaciones pendientes
          </div>
        </div>
        <div class="tableContent">
          <table class="table text-center">
            <thead>
              <tr>
                <th>Evaluacion</th>
                <th>Ponderacion</th>
                <th>Fecha de evaluación</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="evaluacion in evaluacionesSinNotaLaboratorio" :key="evaluacion.id">
                <td>{{evaluacion.nombre}}</td>
                <td>{{evaluacion.ponderacion}}</td>
                <td>{{evaluacion.fechaEvActual}}</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <div class="stateStudent">
          <h4>Estado del estudiante</h4>
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
      evaluacionesSinNotaTeoria:[],
      informacionTeoria: [],
      calificacionesLaboratorio: [],
      evaluacionesSinNotaLaboratorio:[],
      informacionLaboratorio: [],
      mostrar: false,
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
    console.log("ID del usuario:"+ idUsuario + "ID de la asignatura:" + codigoAsig )

    axios
      .get(
        `http://localhost:8000/calificacionesTeoria/${codigoAsig}/${idUsuario}`
      )
      .then(function (response) {
        ins.calificacionesTeoria = response.data[0];
        ins.evaluacionesSinNotaTeoria = response.data[1]
      });
    axios
      .get(
        `http://localhost:8000/calificacionesLaboratorio/${codigoAsig}/${idUsuario}`
      )
      .then(function (response) {
        if (response.data.length != 0) {
          ins.calificacionesLaboratorio = response.data[0];
          ins.evaluacionesSinNotaLaboratorio = response.data[1];
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
