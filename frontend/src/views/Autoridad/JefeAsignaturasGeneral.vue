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
            <th>Nombre Asignatura</th>
              <th>Codigo</th>
              <th>Nivel</th>
              <th>Componente</th>
              <th>Detalle</th>
              <th>Seleccionar</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="asignatura in asignaturas" :key="asignatura.id">
              <td>{{asignatura.id_asignatura.nombre}}</td>
              <td>{{asignatura.id_asignatura.codigo}} </td>
              <td>{{asignatura.id_asignatura.nivel}}</td>
              <td v-if="asignatura.id_asignatura.componente == 'L'">Laboratorio</td>
              <td v-else>Teoria</td>
              <td>
                <button type="button" class="botonTabla" >
                  Detalles
                </button>
              </td>
              <td>
                <button type="button" class="botonTabla" @click="ingresar(asignatura.id_asignatura.id)">
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
  data(){
      return{
          asignaturas: [],
          idJefeCarrera: 0,
      }
  },
  created() {
    // Forma de capturar el id del Jefe de Carrera, dado el id del usuario que inició sesión.
    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;
    axios
    .get(`http://localhost:8000/api/jefeCarrera/${identificacionUsuario}`)
    .then(function (response) {
      ins.idJefeCarrera = response.data.id;
      axios.get(`http://localhost:8000/jefe/${ins.idJefeCarrera}/asignaturas`).then(function (response) {
      ins.asignaturas = response.data;
      });
    });
  },
  mounted(){
    
  },
  methods:{
    ingresar(key){
      router.push(`/jefe/asignaturas/cambios/nota/${key}`)
    }

  }
};
</script>

<style></style>
