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
            Cursos Actuales: numero
          </div>
          <div class="col">
            Evaluaciones Pendientes: numero
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
            Aprobadas: numero
          </div>
          <div class="col">
            Rechazadas: numero
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <h1>Próximas evaluaciones</h1>
        </div>
        <div class="row">
          <div class="col">
            Evaluaciones
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <h1>Próximas calificaciones</h1>
        </div>
        <div class="row">
          <div class="col">

            <table class="tableV2">
              <thead>
                <tr>
                  <th class="row-Nombre">Asignatura</th>
                  <th> Evaluación </th>
                  <th class="row-Horario">Fecha Estimada</th>
                </tr>
              </thead>
            </table>

          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import axios from "axios";


export default {
  components: {
    Sidebar,
    Navbar,
  },
  data() {
    return {
      calificacionesTeoria: [],
      evaluacionesSinNotaTeoria: [],
      calificacionesLaboratorio: [],
      evaluacionesSinNotaLaboratorio: [],
      mostrar: false,
    };
  }
};
</script>

<style>
</style>
