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
        <h3 class="textTitle">Mis Apelaciones</h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Título</th>
              <th>Curso</th>
              <th>Evaluación</th>
              <th>Estado</th>
              <th>Detalle Motivo</th>
              <th>Respuesta</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="solicitud_revision in solicitudes_revision"
              :key="solicitud_revision.id"
            >
              <SolicitudRevision :solicitud_revision="solicitud_revision" />
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarEstudiante.vue";
import Navbar from "../../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    Navbar,
  },
};
</script>

<style></style>
