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
              <th>Seccion</th>
              <th>Profesor</th>
              <th>Horario</th>
              <th>Asignatura</th>
              <th>Seleccionar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="seccion in secciones" :key="seccion.id">
              <td>{{seccion.id_coordinacion.coordinacion}}-{{seccion.id_coordinacion.seccion}}</td>
              <td>{{seccion.id_docente.rut}}-{{seccion.id_docente.dig_verificador}}</td>
              <td>{{seccion.id_coordinacion.bloques_horario}}</td>
              <td>{{seccion.id_coordinacion.id_asignatura.nombre}}</td>
              <td>
                <button type="button" class="btn btn-success" @click.prevent="Ingresar(seccion.id_coordinacion.id)">
                  Seleccionar
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
      console.log(ins.idCoordinador)
      axios.get(`http://localhost:8000/coordinador/coordinacion/${ins.idCoordinador}`).then(function (response) {
        console.log(response.data);
        ins.secciones = response.data;
      });
    });
  },
  methods:{
    Ingresar(key){
      console.log(key)
      router.push(`/coordinador/seccion/solicitudes/${key}`)
    }
  }
};
</script>

<style></style>
