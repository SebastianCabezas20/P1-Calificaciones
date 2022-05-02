<template>
  <div class="flex flex-wrap bg-gray-100 w-full h-screen">
    <Sidebar> </Sidebar>

    <div class="w-5/6 ml-80">
      <Navbar> </Navbar>
      <div class="py-3">
        <div
          class="container-fluid bg-azul-usach rounded-lg"
          id="FondoSuperior"
        >
        listado apelaciones para docente
          <div class="rounded-lg mx-4"></div>
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

<style></style>