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
          <h1>Información dashboard</h1>
        </div>

        <div class="row">
          <div class="col">
            Cursos Totales:
          </div>
          <div class="col">
            Evaluaciones Pendientes:
          </div>
        </div>
        <div class="row">
          <div class="col">
            Solicitudes totales:
          </div>
          <div class="col">
            Solicitudes Pendientes:
          </div>
        </div>
        <div class="row">
          <div class="col">
            Aprobadas:
          </div>
          <div class="col">
            Rechazadas:
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <h1>Cambios en Calificaciones</h1>
        </div>
        <div class="row">
          <div class="col">

            <div class="tableContent">
              <table class="tableV2">
                <thead>
                  <tr>
                    <th>Nombre Evaluación</th>
                    <th>Nombre Asignatura</th>
                    <th>Nombre Alumno</th>
                    <th>Nota Anterior</th>
                    <th>Nota Nueva</th>
                    <th>Motivo</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="cambio_nota in cambio_notas" :key="cambio_nota.id">
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.nombre }}</td>
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_evaluacion.id_coordinacion.id_asignatura.nombre }}</td>
                    <td class="text-center">{{ cambio_nota.id_calificacion.id_estudiante.id_usuario.first_name }}
                      {{ cambio_nota.id_calificacion.id_estudiante.id_usuario.last_name }}</td>
                    
                    <td class="text-center">{{ cambio_nota.anterior_nota }}</td>
                    <td class="text-center">{{ cambio_nota.actual_nota }}</td>
                    <td class="text-center">{{ cambio_nota.motivo }}</td>
                  </tr>
                </tbody>
              </table>
            </div>


          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarCoordinador.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";
import router from "../../router";


export default {
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      cambio_notas:[],
    }
  },
  created() {
    let ins = this;
    axios
      .get(`http://localhost:8000/get/cambiosNota`)
      .then(function (response) {
        console.log(response.data);
        ins.cambio_notas = response.data;
      });
  },
  mounted() {  },
  methods: {  }
};
</script>

<style>
</style>

