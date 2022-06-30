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
        <h3 class="textTitleV2">Cambios de ponderaciones</h3>
      </div>

      <!--Filtros-->
      <div class="row">
        
        <div class="col-3">
          <h5> Seleccione la coordinacion</h5>
          <!-- Botones para la seleccion de coordinaciones -->
          <select v-model="coordinacionesChecked" class="form-select" aria-label="Default select example">
            <option value="">Todas</option>
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
        <div class="col-6">
          <div class="input-group row">
            <span class="input-group-text">Evaluación</span>
            <input type="text" class="form-control" v-model="evaluacionFiltro" placeholder="Evaluación a buscar">
            <span class="input-group-text">Docente</span>
            <input type="text" class="form-control" v-model="docenteFiltro" placeholder="Docente a buscar">
          </div>
        </div>


      </div>

      <div>

      </div>

      <table class="tableV2">
        <thead>
          <tr>
            <th class="row-Codigo">Seccion</th>
            <th class="row-Codigo">Docente</th>
            <th class="row-Codigo">Evaluacion</th>
            <th class="row-Codigo">Ponderacion anterior</th>
            <th class="row-Codigo">Ponderacion actual</th>
            <th class="row-Codigo">Fecha del cambio</th>
            <th class="row-Codigo">Motivo</th>
          </tr>
        </thead>
        <tbody>
          <template
            v-for="cambio in cambios"
            :key="cambio.id"
          >
            <tr v-show="filterSecciones(cambio.id_evaluacion.id_coordinacion.seccion,
            cambio.id_evaluacion.id_coordinacion.coordinacion) &&
             filterEvaluacion(cambio.id_evaluacion.nombre) && filterDocente(cambio.id_evaluacion.id_docente.id_usuario.first_name,cambio.id_evaluacion.id_docente.id_usuario.last_name)">
              <td>{{ cambio.id_evaluacion.id_coordinacion.coordinacion }}-{{cambio.id_evaluacion.id_coordinacion.seccion}}</td>
              <td>{{cambio.id_evaluacion.id_docente.id_usuario.first_name}} {{cambio.id_evaluacion.id_docente.id_usuario.last_name}}</td>
              <td>{{ cambio.id_evaluacion.nombre }}</td>
              <td>{{ cambio.ponderacionAnterior * 100 }}%</td>
              <td>{{ cambio.ponderacionNueva * 100}}%</td>
              <td>{{ cambio.fecha_cambio }}</td>
              <td>{{ cambio.motivo }}</td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarJefeCarrera.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  props:['idAsignatura'],
  data() {
    return {
      cambios: [],
      secciones:[],
      coordinaciones:[],
      seccionesChecked:"",
      coordinacionesChecked:"",
      evaluacionFiltro:'',
      docenteFiltro:'',

    };
  },
  mounted() {
    let ins = this
    let idAsignaturaURL = this.idAsignatura
    axios.get(`http://localhost:8000/get/cambio/ponderacion/asignatura/${idAsignaturaURL}`)
    .then(function (response) {
      console.log(response.data);
      ins.cambios = response.data[0];
      ins.coordinaciones = response.data[1]
      ins.secciones = response.data[2]
      //ins.coordinacionesChecked = response.data[1]
      //ins.seccionesChecked = response.data[2]
    });
  },
  methods: {
    filterSecciones(seccion,coordinacion){ 
      if((this.seccionesChecked.includes(seccion) && this.coordinacionesChecked.includes(coordinacion)) ||
      (this.seccionesChecked == "" && this.coordinacionesChecked == "")){
        return true
      }
      else{
        return false
      }
    },
    filterEvaluacion(evaluacion){
      let n = Array(evaluacion)
      return n[0].toLocaleLowerCase().indexOf(this.evaluacionFiltro.toLocaleLowerCase()) >= 0
    },
    filterDocente(nombre,apellido){
      let n = Array(nombre+' '+apellido)
      console.log(n)
      return n[0].indexOf(this.docenteFiltro) >= 0
    }
  },
};
</script>

<style></style>
