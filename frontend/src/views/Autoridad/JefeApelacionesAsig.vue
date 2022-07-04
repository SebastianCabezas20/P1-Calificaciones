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
        

        <div class="col-3">
          <h5> Seleccione la coordinacion</h5>
          <!-- Botones para la seleccion de coordinaciones -->
          <select v-model="coordinacionesChecked" class="form-select" aria-label="Default select example">
            <option selected value="">Todas</option>
            <option  v-for="(coordinacion,index) in coordinaciones" :key="index">{{coordinacion}}</option>
          </select>
        </div>
        
        <div class="col-3">
          <!-- Botones para la seleccion de secciones -->
          <h5> Seleccione la sección</h5>
          <select  v-model="seccionesChecked" class="form-select" aria-label="Default select example">
            <option value="" >Todas</option>
            <option v-for="(seccion,index) in secciones" :key="index" >{{seccion}}</option>
          </select>
        </div>

        <!--Grupo de inputs para ingresar nombre de evaluacion y profesor-->
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Evaluación</span>
            <input type="text" class="form-control" v-model="evaluacionFiltro" placeholder="Evaluación a buscar">
            <span class="input-group-text">Docente</span>
            <input type="text" class="form-control" v-model="docenteFiltro" placeholder="Docente a buscar">
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
            <div class="btn-group" role="group" aria-label="Basic checkbox toggle button group" style="margin-left:30px">
              <input type="checkbox" class="btn-check" v-model="revisions" value="E" id="revision" autocomplete="off">
              <label class="btn btn-outline-primary" for="revision"> En revision</label>
            </div>
          </div>
        </div>
        </div>


      </div>
      <div class="tableContent">
        <table class="tableV2">
          <thead>
            <tr>
              <th>Nombre Evaluacion</th>
              <th>Estado</th>
              <th>Fecha Creacion</th>
              <th>Estudiante</th>
              <th>Seccion</th>
              <th>Docente</th>
              <th>Detalle</th>
            </tr>
          </thead>
          <tbody v-for="solicitud in solicitudes" :key="solicitud.id">
            <ApelacionesAsignaJefe :solicitud="solicitud" :coordinaciones="this.coordinacionesChecked" :secciones="this.seccionesChecked"
            :nombreEvaluacion="this.evaluacionFiltro"
            :pendiente="this.pendientes" :revision="this.revisions" :aprobada="this.aprobadas" :rechazada="this.rechazadas" :nombreDocente="this.docenteFiltro"/>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarJefeCarrera.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import ApelacionesAsignaJefe from '../../components/ApelacionesAsignaJefe.vue';


export default {
  components: {
    Sidebar,
    Navbar,
    ApelacionesAsignaJefe
},
props:['idAsignatura'],
  data(){
      return{
          solicitudes: [],
          secciones:[],
          coordinaciones:[],
          seccionesChecked:'',
          coordinacionesChecked:'',
          evaluacionFiltro:'',
          docenteFiltro:'',
          aprobadas: true,
          rechazadas: true,
          pendientes: true,
          revisions:true,
      }
  },
  created() {
    let ins = this;
    let IDasignatura  = this.idAsignatura;
    axios.get(`http://localhost:8000/jefe/asignatura/solicitudes/${IDasignatura}`).then(function (response) {
      ins.solicitudes = response.data[0];
      ins.coordinaciones = response.data[1];
      ins.secciones = response.data[2]
    });
  },
 
};
</script>

<style></style>
