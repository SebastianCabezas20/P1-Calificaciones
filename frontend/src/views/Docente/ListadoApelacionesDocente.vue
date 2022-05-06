<template>
  <div>
    <Navbar> </Navbar>
  </div>

  <div>
    <Sidebar> </Sidebar>
  </div>

  <div class="contentViews">
    <div class="centralContent">
      <div class="container-fluid bg-azul-usach rounded-lg" id="FondoSuperior">
        listado apelaciones para docente
        <div class="rounded-lg mx-4"></div>
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
