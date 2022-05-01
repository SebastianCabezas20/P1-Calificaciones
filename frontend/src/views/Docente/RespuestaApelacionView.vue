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
    <div class="flex flex-wrap bg-gray-100 w-full h-screen">
      <Sidebar></Sidebar>

      <div class="w-5/6">
        <Navbar> </Navbar>
        
        <div class="container" id="texto">
          <h4 style="background-color: #00adb5; padding: 10px">
            Responder Apelacion
          </h4>
        </div>
        <div class="container-fluid" id="contenedorRespuesta">
          <div
            class="container"
            style="position: absolute; margin-top: 50px; margin-left: 50px"
          >
            <h6>Titulo de evaluacion</h6>
            <h6>Nombre asignatura</h6>
            <h6>Nota</h6>
          </div>
          <form
            style="position: absolute; margin-top: 170px; margin-left: 50px"
          >
            <input
              class="form-control"
              type="text"
              value="Nombre del Estudiante"
              disabled
              readonly
              style="width: 700px"
            />
            <label
              for="ApelacionContenido"
              class="form-label"
              style="margin-top: 10px"
              >Apelacion del Estudiante</label
            >
            <textarea
              class="form-control"
              id="ApelacionContenido"
              rows="4"
              disabled
              readonly
            >
Apelacion del Estudiante</textarea
            >
            <label for="Respuesta" class="form-label" style="margin-top: 20px"
              >Respuesta</label
            >
            <textarea class="form-control" id="ContenidoRespuesta" rows="5">
Respuesta del Docente</textarea
            >
            <div class="form-check" style="margin-top: 20px">
              <input
                class="form-check-input"
                type="radio"
                name="Estado"
                id="RadioAceptar"
                value="Aceptado"
              />
              <label class="form-check-label" for="RadioAceptar">
                Aceptar
              </label>
            </div>
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="Estado"
                id="RadioRechazar"
                value="Rechazado"
              />
              <label class="form-check-label" for="RadioRechazar">
                Rechazar
              </label>
            </div>
            <button class="btn btn-primary" type="" style="margin-top: 30px">
              Enviar Respuesta
            </button>
          </form>
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
div#contenedorRespuesta {
  height: 800px;
  width: 900px;
  background-color: #bac5c4;
  position: relative;
}
</style>
