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
        <h4 class="textTitleV2">Solicitudes de revisión por coordinación</h4>
      </div>
        <table class="tableV2">
          <thead>
            <tr>
              <th class="row-Codigo">Sección</th>
              <th class="row-Asignatura">Asignatura</th>
              <th>Docente</th>
              <th>Horario</th>
              <th>Seleccionar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="seccion in secciones" :key="seccion.id">
                <td>{{seccion[0].id_coordinacion.coordinacion}}-{{seccion[0].id_coordinacion.seccion}}</td>
                <td>{{seccion[0].id_coordinacion.id_asignatura.nombre}}</td> 
                <!--V-for para obtener todas las tuplas con los distintos profesores-->
                <td> 
                  <label class="row" v-for="s in seccion" :key="s.index" >
                    {{s.id_docente.id_usuario.first_name}} {{s.id_docente.id_usuario.last_name}}
                  </label>
                </td>
                <td>{{seccion[0].id_coordinacion.bloques_horario}}</td>
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
import Sidebar from "../../components/SidebarCoordinador.vue";
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
          idCoordinador:0,
      }
  },
  created() {
    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
    .get(`http://localhost:8000/api/coordinador/${identificacionUsuario}`)
    .then(function (response) {
      ins.idCoordinador = response.data.id;
      axios.get(`http://localhost:8000/coordinador/coordinacion/${ins.idCoordinador}`).then(function (response) {
        // Se obtienen las coordinaciones en un arreglo [[Co1],[Co2],[Co3]]
        ins.secciones = response.data;
      });
    });
  },
  methods:{
    Ingresar(key){
      router.push(`/coordinador/seccion/solicitudes/${key}`)
    }
  }
};
</script>

<style></style>
