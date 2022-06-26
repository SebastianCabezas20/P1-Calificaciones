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
        <h3 class="textTitleV2">Asignaturas</h3>
      </div>

      <table class="tableV2">
          <thead>
            <tr>
              <th>Seccion</th>
              <th>Profesor</th>
              <th>Horario</th>
              <th>Asignatura</th>
              <th>Seleccionar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="seccion in secciones" :key="seccion.id">
                <td>{{seccion[0].id_coordinacion.coordinacion}}-{{seccion[0].id_coordinacion.seccion}}</td>
                <!--V-for para obtener todas las tuplas con los distintos profesores-->
                <td> 
                  <label class="row" v-for="s in seccion" :key="s.index" >
                    {{s.id_docente.id_usuario.first_name}} {{s.id_docente.id_usuario.last_name}}
                  </label>
                </td>
                <td>{{seccion[0].id_coordinacion.bloques_horario}}</td>
                <td>{{seccion[0].id_coordinacion.id_asignatura.nombre}}</td>    
                <td>
                  <button type="button" class="botonTabla" @click.prevent="Ingresar(seccion[0].id_coordinacion.id)">
                    Seleccionar
                  </button>
                </td>              
            </tr>
          </tbody>
        </table>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarJefeCarrera.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  props:["idAsignatura"],
  data(){
      return{
          secciones: [],
      }
  },
  created() {
    // Forma de capturar el id del Jefe de Carrera, dado el id del usuario que inició sesión.
    let ins = this;
    let identificacionAsignatura = this.idAsignatura
    axios
    .get(`http://localhost:8000/get/secciones/asignatura/${identificacionAsignatura}`)
    .then(function (response) {
      ins.secciones = response.data;
    });
  },
  mounted(){
    
  },
  methods:{
    Ingresar(key){
        router.push(`/jefe/visualizacion/secciones/evaluaciones/${key}/${this.idAsignatura}`)
    }

  }
};
</script>

<style></style>
