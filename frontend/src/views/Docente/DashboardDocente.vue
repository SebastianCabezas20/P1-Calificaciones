<template>
  <div class="flex flex-wrap bg-gray-100 w-full h-screen">
    <Sidebar> </Sidebar>

    <div class="w-5/6">
      <Navbar> </Navbar>
      <p>Contenido aquí del docente...</p>
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