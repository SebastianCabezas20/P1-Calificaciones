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
        <h4 class="textTitle">Apelaciones</h4>
      </div>
      <!--Filtros-->
      <div class="row">
  
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Evaluación</span>
            <input type="text" class="form-control" v-model="evaluacionFiltro" placeholder="Evaluación a buscar">
            <span class="input-group-text">Docente</span>
            <input type="text" class="form-control" v-model="docenteFiltro" placeholder="Docente a buscar">
          </div>
        </div>
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Estudiante</span>
            <input type="text" class="form-control" v-model="estudianteFiltro" placeholder="Evaluación a buscar">
          </div>
          <div class="input-group row">
          <h6> Tipo de apelaciones</h6>
          <!-- Botones para la seleccion de estados -->
          <div>
            <div class="btn-group" role="group" aria-label="Basic checkbox toggle button group">
              <input type="checkbox" class="btn-check" v-model="rechazadas" value="R" id="rechazada" autocomplete="off">
              <label class="btn btn-outline-primary" for="rechazada"> Rechazadas</label>
            </div>
            <div class="btn-group" role="group" aria-label="Basic checkbox toggle button group" style="margin-left:30px">
              <input type="checkbox" class="btn-check" v-model="aprobadas" value="A" id="aprobadas" autocomplete="off">
              <label class="btn btn-outline-primary" for="aprobadas"> Aprobadas</label>
            </div>
            <div class="btn-group" role="group" aria-label="Basic checkbox toggle button group" style="margin-left:30px">
              <input type="checkbox" class="btn-check" v-model="pendientes" value="P" id="pendiente" autocomplete="off">
              <label class="btn btn-outline-primary" for="pendiente"> Pendientes</label>
            </div>
          </div>
        </div>
        </div>


      </div>

      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Nombre Evaluacion</th>
              <th>Profesor</th>
              <th>Estado</th>
              <th>Fecha Creacion</th>
              <th>Estudiante</th>
              <th>Detalle</th>
            </tr>
          </thead>
          <tbody v-for="solicitud in solicitudes" :key="solicitud.id">
            <ApelacionesCoordinador :solicitud="solicitud" :pendiente="this.pendientes" :aprobada="this.aprobadas" :rechazada="this.rechazadas"
            :evaluacionFiltro="this.evaluacionFiltro" />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import ApelacionesCoordinador from "../../components/ApelacionesCoordinador.vue";
import router from "../../router";


export default {
  components: {
    Sidebar,
    Navbar,
    ApelacionesCoordinador
},
props:['idCurso'],
  data(){
      return{
          solicitudes: [],
          estudianteFiltro:'',
          evaluacionFiltro:'',
          docenteFiltro:'',
          aprobadas: true,
          rechazadas: true,
          pendientes: true
          
      }
  },
  created() {
    let ins = this;
    let IDcurso = this.idCurso;
    axios.get(`http://localhost:8000/coordinacion/solicitudes/${IDcurso}`).then(function (response) {
      console.log(response.data);
      ins.solicitudes = response.data;
    });
},
};
</script>

<style></style>
