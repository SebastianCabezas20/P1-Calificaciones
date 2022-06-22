<template>
  <div id="navbar">
    <div>
      <p class="textNavbar">Gestión y Control de Calificaciones</p>
    </div>
    <div>
      <p class="textNavbar">{{ nombreUsuario }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nombreUsuario: "",
    };
  },
  mounted() {
    this.nombreUsuario = this.$store.getters.nameUser;
  },
};
</script>

<style>
#navbar {
  background-color: #f38a24;
  height: 60px;
  padding: 0px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-left: 260px;
}

.textNavbar {
  font-family: "Inter", sans-serif;
  color: #fff;
  font-weight: 600;
  font-size: 22px;
  padding-top: 15px;
}
</style>
