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

div#FondoSuperior {
  background: #00adb5;
  border-radius: 5px;
  width: 1200px;
  padding: 10px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  position: relative;
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
