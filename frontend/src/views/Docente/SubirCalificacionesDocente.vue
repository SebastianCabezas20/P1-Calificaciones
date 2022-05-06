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
        <h3 class="textTitle">Subida de Calificaciones: -nombre Curso-</h3>
      </div>
      <div class="tableContent">
        <table class="table">
          <thead>
            <tr>
              <th>Rut</th>
              <th>Nombre</th>
              <th>Evaluación</th>
              <th>Estado</th>
              <th>Observación</th>
              <th>Calificación</th>
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

<style>
div#apelacion {
  position: absolute;
  background: #eeeeee;
  margin-top: 130px;
  margin-left: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  width: 500px;
  height: 350px;
  overflow-y: auto;
  overflow-x: hidden;
}

div#curso {
  background: #eeeeee;
  margin-top: 125px;
  margin-left: 20px;
  padding: 0;
  display: inline-block;
  position: absolute;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}
</style>
