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
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Nombre Evaluacion</th>
              <th>Estado</th>
              <th>Fecha Creacion</th>
              <th>Estudiante</th>
              <th>Fecha Respuesta</th>
              <th>Detalle</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="solicitud in solicitudes" :key="solicitud.id">
              <td>{{solicitud.id_evaluacion.nombre}}</td>
              <td>{{ solicitud.estado}} </td>
              <td>{{solicitud.fecha_creacion}}</td>
              <td>{{solicitud.id_estudiante.id_usuario.username}}</td>
              <td>{{solicitud.fecha_respuesta}}</td>
              <td>
                <button type="button" class="btn btn-success">
                  Detalles
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarAutoridad.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';

export default {
  components: {
    Sidebar,
    Navbar,
  },
  data(){
      return{
          solicitudes: []
      }
  },
  created() {
    let ins = this;
    axios.get("http://localhost:8000/jefe/asignatura/solicitudes").then(function (response) {
      console.log(response.data);
      ins.solicitudes = response.data;
    });
},
};
</script>

<style></style>
