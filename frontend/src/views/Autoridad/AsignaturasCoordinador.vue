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
        <h4 class="textTitleV2">Coordinaciones</h4>
      </div>
        <table class="tableV2">
          <thead>
            <tr>
              <th>Código</th>
              <th>Asignatura</th>
              <th>Componente</th>
              <th>Profesor</th>
              <th>Horario</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="seccion in secciones" :key="seccion.id">
              <td>{{seccion[0].id_coordinacion.id_asignatura.codigo}}-{{seccion[0].id_coordinacion.coordinacion}}-{{seccion[0].id_coordinacion.seccion}}</td>
              <td>{{seccion[0].id_coordinacion.id_asignatura.nombre}}</td>
              <td v-if="seccion[0].id_coordinacion.id_asignatura.componente == 'T'">Teoría</td>
              <td v-else>Laboratorio</td>
              <td><!--V-for para obtener todas las tuplas con los distintos profesores-->
                <label class="row" v-for="s in seccion" :key="s.index">
                  {{s.id_docente.id_usuario.first_name}} {{s.id_docente.id_usuario.last_name}}
                </label>
              </td>
              <td>{{seccion[0].id_coordinacion.bloques_horario}}</td>
              <td>
                <button 
                  type="button" 
                  class="botonTabla"
                  @click="getCoordinacion($event, seccion[0].id_coordinacion.id_asignatura.id, seccion[0].id_coordinacion.id)"
                  >
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
import Sidebar from "../../components//SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  data(){
      return{
          secciones: [],
          idCoordinador: 0,
      }
  },
  created() {
    // Forma de capturar el id del Coordinador, dado el id del usuario que inició sesión.
    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
    .get(`http://localhost:8000/api/coordinador/${identificacionUsuario}`)
    .then(function (response) {
      ins.idCoordinador = response.data.id;
      axios.get(`http://localhost:8000/coordinador/coordinacion/${ins.idCoordinador}`).then(function (response) {
        console.log(response.data);
        // Se obtienen las coordinaciones en un arreglo [[Co1],[Co2],[Co3]]
        ins.secciones = response.data;
      });
    });
  },
  methods: {
    getCoordinacion(event, idAsignatura, idCoordinacion){
      this.$router.push({ path: `/coordinador/asignatura/${idAsignatura}/seccion/${idCoordinacion}` });
    },
  },
};
</script>

<style></style>
