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
        <h4 class="textTitle">Cambio de calificaciones</h4>
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
      </div>

      <div class="tableContent">
        <table class="tableV2">
                <thead>
                  <tr>
                    <th>Nombre Evaluación</th>
                    <th>Nombre Asignatura</th>
                    <th>Nombre Alumno</th>
                    <th>Nombre profesor</th>
                    <th>Fecha cambio</th>
                    <th>Nota Anterior</th>
                    <th>Nota Nueva</th>
                    <th>Motivo</th>
                  </tr>
                </thead>
                <tbody>
                <template v-for="cambio_nota in cambio_notas" :key="cambio_nota.id">
                  <tr v-show="filterEvaluacion(cambio_nota.id_calificacion.id_evaluacion.nombre)">
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.nombre }}</td>
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_estudiante.id_usuario.first_name }}
                      {{ cambio_nota.id_calificacion.id_estudiante.id_usuario.last_name }}</td>
                      <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.id_docente.id_usuario.first_name }}
                      {{ cambio_nota.id_calificacion.id_evaluacion.id_docente.id_usuario.last_name }}</td>
                    <td class="text-center">{{ cambio_nota.fecha_cambio }}</td>
                    <td class="text-center">{{ cambio_nota.anterior_nota }}</td>
                    <td class="text-center">{{ cambio_nota.actual_nota }}</td>
                    <td class="text-center">{{ cambio_nota.motivo }}</td>
                  </tr>
                </template>
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
          cambio_notas: [],
          estudianteFiltro:'',
          evaluacionFiltro:'',
          docenteFiltro:'',          
      }
  },
  created() {
    let ins = this;
    let IDcurso = this.idCurso;
    axios.get(`http://localhost:8000/get/cambio/calificacion/curso/${IDcurso}`).then(function (response) {
      console.log(response.data);
      ins.cambio_notas = response.data;
    });
    },
    methods: {
    filterEvaluacion(evaluacion){
      let n = Array(evaluacion)
      return n[0].toLocaleLowerCase().indexOf(this.evaluacionFiltro) >= 0
    }
  },
};
</script>

<style></style>
