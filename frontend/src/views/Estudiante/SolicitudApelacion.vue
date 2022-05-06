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
          <h3 class="textTitle">Solicitud de Apelación</h3>
        </div>

        <div id="formApelacion">
          <h5 class="formText">Titulo de la Evaluación</h5>
          <h5 class="formText">Nombre de la asignatura</h5>
          <h5 class="formText">Nota</h5>
          <h5 class="formText">Profesor:</h5>
          <h5 class="formText">Motivo de la solicitud</h5>

          <textarea
            placeholder="Escriba acá su solicitud"
            id="motivoSolicitud"
          ></textarea>

          <div class="divbuttonForm">
            <button class="buttonForm">Apelar</button>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import Sidebar from "../../components/SidebarEstudianteDocente.vue";
import Navbar from "../../components/NavbarGeneral.vue";
import InformacionCurso from "../../components/InformacionCurso.vue";
import CalificacionInfo from "../../components/Calificacion.vue";

export default {
  components: {
    Sidebar,
    Navbar,
    InformacionCurso,
    CalificacionInfo,
  },
};
</script>

<style>
#formApelacion {
  background: #eeeeee;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  width: 50%;
  overflow-y: auto;
  overflow-x: hidden;
  border-radius: 5px;
  padding: 20px;
}

.formText {
  display: block;
}

.divbuttonForm {
  display: block;
  margin-top: 10px;
  background-color: #004883;
  border: 2px solid #fff;
  border-radius: 5px;
  width: 25%;
  text-align: center;
}

.buttonForm {
  font-weight: bold;
  color: #fff;
  padding: 10px 15px;
}

#motivoSolicitud {
  display: block;
  width: 95%;
  border: 1px solid #004883;
}

div#contenidoApelación {
  background-color: #eeeeee;
  position: absolute;
  display: inline-block;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  position: absolute;
  padding-left: 30px;
  bottom: 0;
  margin-bottom: 20px;
  margin-left: 20px;
}
</style>
