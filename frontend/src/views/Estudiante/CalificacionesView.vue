<template>
  <div class="flex flex-wrap bg-gray-100">
    <Sidebar></Sidebar>

    <div class="w-5/6 ml-80">
      <Navbar> </Navbar>

      <div class="py-3">
        <div class="container-fluid bg-azul-usach rounded-lg" id="FondoSuperior">
          <div class="rounded-lg mx-4">
            <InformacionCurso />
          </div>
        </div>

        <div class="container-fluid rounded-lg bg-azul-usach" id="ParteInferior">
          <div class="col-11" id="informacion">
            <h3 id="titulo" class="pl-3">
              Calificaciones Catedra
            </h3>
          </div>
          <div class="table-responsive" id="tabla">
            <table class="table">
              <thead id="a">
                <tr>
                  <th>Evaluacion</th>
                  <th>Observacion</th>
                  <th>Calificacion</th>
                  <th>Ponderacion</th>
                  <th>Estado</th>
                  <th>Fecha</th>
                  <th>Apelar</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="i in 5" :key="i">
                  <CalificacionInfo />
                </tr>
              </tbody>
            </table>
          </div>
          <div id="estadoEstudiante" class="col-11">
            <h4>Estado del estudiante</h4>
          </div>
        </div>
        <br />

        <div class="container-fluid rounded-lg bg-azul-usach" id="ParteInferior">
          <div class="col-11" id="informacion">
            <h3 id="titulo" style="padding-left: 50px">
              Calificaciones laboratorio
            </h3>
          </div>
          <div class="table-responsive" id="tabla">
            <table class="table">
              <thead id="a">
                <tr>
                  <th>Evaluacion</th>
                  <th>Observacion</th>
                  <th>Calificacion</th>
                  <th>Ponderacion</th>
                  <th>Estado</th>
                  <th>Fecha</th>
                  <th>Apelar</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="i in 5" :key="i">
                  <CalificacionInfo />
                </tr>
              </tbody>
            </table>
          </div>
          <div id="estadoEstudiante" class="col-11">
            <h4>Estado del estudiante</h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";

export default {
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
};
</script>

<style>
div#tabla {
  position: absolute;
  background: #eeeeee;
  margin-top: 130px;
  margin-left: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  width: 1100px;
  height: 300px;
  overflow-y: auto;
  overflow-x: hidden;
}

thead#a tr th {
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: #F38A24 !important;
}
div#FondoSuperior {
  width: 1200px;
  padding: 10px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  position: relative;
}

div#ParteInferior {
  width: 1200px;
  height: 575px;
  position: relative;
  margin-top: 50px;
}

#informacion {
  background: #eeeeee;
  margin-top: 30px;
  margin-left: 20px;
  display: inline-block;
  position: absolute;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
}

div#estadoEstudiante {
  background-color: #eeeeee;
  position: absolute;
  display: inline-block;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  position: absolute;
  padding-left: 30px;
  bottom: 0;
  margin-bottom: 20px;
  margin-left: 20px;
}
</style>
