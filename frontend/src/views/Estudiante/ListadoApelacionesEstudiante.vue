<template>
  <head>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
  </head>
  <body>
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
  </body>
</template>

<script>
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    Navbar,
  },
};
</script>

<style></style>
