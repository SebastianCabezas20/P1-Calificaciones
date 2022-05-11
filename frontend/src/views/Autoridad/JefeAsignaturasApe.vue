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
              <th>Nombre Asignatura</th>
              <th>Codigo</th>
              <th>Nivel</th>
              <th>Componente</th>
              <th>Coordinador</th>
              <th>Detalle</th>
              <th>Seleccionar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="asignatura in asignaturas" :key="asignatura.id">
              <td>{{asignatura.id_asignatura.nombre}}</td>
              <td>{{asignatura.id_asignatura.codigo}} </td>
              <td>{{asignatura.id_asignatura.nivel}}</td>
              <td>{{asignatura.id_asignatura.componente}}</td>
              <td>{{asignatura.id_asignatura.id_coordinador.id_usuario.username}}</td>
              <td>
                <button type="button" class="btn btn-success">
                  Detalles
                </button>
              </td>
              <td>
                <button type="button" class="btn btn-success" @click="Ingresar(asignatura.id_asignatura.id)">
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
import Sidebar from "../../components/SidebarAutoridad.vue";
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
          asignaturas: []
      }
  },
  created() {
    let ins = this;
    // ID JEFE DE CARRERA PARA MOSTRAR SUS ASIGNATURAS
    axios.get("http://localhost:8000/jefe/1/asignaturas").then(function (response) {
      console.log(response.data);
      ins.asignaturas = response.data;
    });
  },
  methods:{
    Ingresar(key){
      console.log("holas")
      router.push(`/jefe/asignaturas/apelaciones/${key}`)
    }
  }
};
</script>

<style></style>
