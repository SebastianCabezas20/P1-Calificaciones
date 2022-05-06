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
        <h3 class="textTitle">
          Modificacion de Calificaciones: -nombre Curso-
        </h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Rut</th>
              <th>Nombre</th>
              <th>Evaluación</th>
              <th>Nota Actual</th>
              <th>Observación</th>
              <th>Nueva Calificación</th>
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
import Sidebar from "../../components/SidebarDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    Navbar,
  },
};
</script>

<style></style>
