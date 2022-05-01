<template>
  <div class="flex flex-wrap bg-gray-100 h-screen">
    <Sidebar></Sidebar>

    <div class="w-5/6 ml-80">
      <Navbar> </Navbar>

      <div class="flex items-center justify-center w-full">
        <div class="border-2 border-azul-usach my-5 bg-gris-usach">
          <div class="text-start text-xl font-bold mt-3">
            <h4 class="p-2">Responder Apelacion</h4>
          </div>

          <div class="bg-gris-usach" id="contenedorRespuesta">
            <div class="p-2 space-y-2">
              <h6>Titulo de evaluacion</h6>
              <h6>Nombre asignatura</h6>
              <h6>Nota</h6>
            </div>

            <form class="px-2 py-5 space-y-4">
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
              <textarea class="form-control relative block w-full" id="ContenidoRespuesta" rows="5">
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
              <button class="roup relative w-full flex justify-center py-2 px-4 border border-transparent text-md font-medium rounded-lg text-white bg-azul-usach hover:bg-azulHoverUsach focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Enviar Respuesta
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
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
}
</style>
