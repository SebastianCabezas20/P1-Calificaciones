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
        <h4 class="textTitle">Responder Apelacion</h4>
      </div>

      <div class="formApelacion">
        <h6 class="textoFormulario">Titulo de evaluacion</h6>
        <h6 class="textoFormulario">Nombre asignatura</h6>
        <h6 class="textoFormulario">Nota</h6>

        <form>
          <input
            class="form-control relative block w-full"
            type="text"
            value="Nombre del Estudiante"
            disabled
            readonly
          />
          <label
            class="form-label relative block w-full"
            for="ApelacionContenido"
            >Apelacion del Estudiante</label
          >
          <textarea
            class="form-control relative block w-full"
            id="ApelacionContenido"
            rows="4"
            disabled
            readonly
          >
    Apelacion del Estudiante</textarea
          >
          <label for="Respuesta" class="form-label relative block w-full"
            >Respuesta</label
          >
          <textarea
            class="form-control relative block w-full"
            id="ContenidoRespuesta"
            rows="5"
          >
    Respuesta del Docente</textarea
          >
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="Estado"
              id="RadioAceptar"
              value="Aceptado"
            />
            <label class="form-check-label" for="RadioAceptar"> Aceptar </label>
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

          <button class="buttonForm">Enviar Respuesta</button>
        </form>
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
