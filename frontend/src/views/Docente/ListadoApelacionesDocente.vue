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
        <h3 class="textTitle">
          Solicitudes de Apelacion
        </h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Asignatura</th>
              <th>Evaluacion</th>
              <th>Motivo</th>
              <th>Accion</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="solicitud in solicitudes" :key="solicitud.id">
              <tr scope="row" v-if="solicitud.id_docente.id === idDocente">
                <SolicitudesDocente :solicitud_revision="solicitud"
                @EventIdEvaluacion="(idEstudiante,idEvaluacion) => ingresar(idEstudiante,idEvaluacion)" />
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
import SolicitudesDocente from "../../components/SolicitudesDocente.vue";
import axios from "axios";
import router from '../../router';

export default{
  components: {
    Sidebar,
    Navbar,
    SolicitudesDocente,
  },
  data() {
    return {
      solicitudes: [],
      idDocente: 0,
    };
  },
  mounted() {
    let identificacionUsuario = this.$store.getters.idUsuario;
    let ins = this;
    axios
      .get(`http://localhost:8000/api/docente/${identificacionUsuario}`)
      .then(function (response) {
        ins.idDocente = response.data.id;
        console.log(ins.idDocente);
      });
    axios
      .get(`http://localhost:8000/solicitudesDocente`)
      .then(function (response) {
        console.log(response.data);
        ins.solicitudes = response.data;
    });
  },
  methods:{/// Para conectar se necesita idEstudiante y idEvaluacion de esa apelacion
    ingresar(idEst,idEval){
      console.log(idEst)
      console.log(idEval)
      router.push(`/docente/apelacion/answer/${idEst}/${idEval}`)
    }

    
  }
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
