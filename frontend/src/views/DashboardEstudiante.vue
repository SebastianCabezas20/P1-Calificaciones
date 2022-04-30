<template>
  <div class="flex flex-wrap bg-gray-100 w-full h-screen">
    <Sidebar> </Sidebar>
    <NavbarGeneral> </NavbarGeneral>
  </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";
import NavbarGeneral from "../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    NavbarGeneral,
  },
};
</script>

<style></style>
