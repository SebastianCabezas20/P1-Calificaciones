<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">

      <div class="container">
        <div class="row">
          <h1>Datos generales Departamento</h1>
        </div>

        <div class="row">
          <div class="col">
            Cambios notas en semestre: {{ Number(Info[0]) }}
          </div>
          <div class="col">
            Cambios notas a azules en semestre: {{ Number(Info[1]) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Cambios notas a rojos en semestre: {{ Number(Info[2]) }}
          </div>
          <div class="col">
            Cambios en ponderaciones: {{ Number(Info[3]) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Cambio fechas: {{ Number(Info[4]) }}
          </div>
          <div class="col">
            Solicitudes: {{ Number(Info[5]) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes pendientes: {{ Number(Info[6]) }}
          </div>
          <div class="col">
            Solicitudes aprobadas: {{ Number(Info[7]) }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes rechazadas: {{ Number(Info[8]) }}
          </div>
        </div>
      </div>
      
    </div>

  </div>


</template>

<script>
import Sidebar from "../../components/SidebarAutoridad.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from 'axios';
import router from "../../router";
import Chart from 'chart.js/auto';



export default {
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      Info: []
    }
  },
  created() {
    let ins = this;
    let identificacionUsuario = this.$store.getters.idUsuario;

    axios
      .get(`http://localhost:8000/get/infodashboardautoridadsub/${identificacionUsuario}`)
      .then(function (response) {
        ins.Info = response.data;
      });
  },
};
</script>

<style>
</style>
