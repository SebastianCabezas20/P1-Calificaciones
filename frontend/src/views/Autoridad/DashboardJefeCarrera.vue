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
        <h4 class="textTitle">Cambios de Fecha</h4>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Nombre Evaluación</th>
              <th>Nombre Asignatura</th>
              <th>Docente</th>
              <th>Fecha Anterior</th>
              <th>Fecha Nueva</th>
              <th>Motivo</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="cambio_fecha in cambio_fechas" :key="cambio_fecha.id">
              <td class="text-center">{{cambio_fecha.id_evaluacion.nombre}}</td>
              <td class="text-center">{{cambio_fecha.id_evaluacion.id_coordinacion.id_asignatura.nombre}}</td>
              <td class="text-center">{{cambio_fecha.id_evaluacion.id_docente.id_usuario.first_name}} {{cambio_fecha.id_evaluacion.id_docente.id_usuario.last_name}}</td>
              <td class="text-center">{{cambio_fecha.fechaAnterior}}</td>
              <td class="text-center">{{cambio_fecha.fechaNueva}}</td>
              <td class="text-center">{{cambio_fecha.motivo}}</td>
            </tr>
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
import router from "../../router";

export default {
  components: {
    Sidebar,
    Navbar,
  },
  data(){
      return{
          cambio_fechas: [],
      }
  },
  created() {
    // Forma de capturar el id del Jefe de Carrera, dado el id del usuario que inició sesión.
    let ins = this;
    axios
    .get(`http://localhost:8000/get/cambiosFecha`)
    .then(function (response) {
      console.log(response.data);
      ins.cambio_fechas = response.data;
    });
  },
  mounted() {

  },
  methods: {

  }
};
</script>

<style></style>
