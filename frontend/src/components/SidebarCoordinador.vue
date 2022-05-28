<template>
  <div class="wrapper">
    <div class="sidebar">
      <div class="logo">
        <div>
          <img src="../assets/Usach-Trans.png" alt="Logo Usach" />
        </div>
      </div>

      <ul>
        <li>
          <a href="/coordinador/home">
            <span class="icon"><i class="fa-solid fa-house"></i></span>
            <span>Inicio</span>
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon"><i class="fa-solid fa-user"></i></span>
            <span>Mi Cuenta</span>
          </a>
        </li>
        <li>
          <a href="/coordinador/asignaturas/general">
            <span class="icon"><i class="fa-solid fa-book"></i></span>
            <span>Coordinaciones</span>
          </a>
        </li>
        <li>
          <a href="/coordinador/seccion">
            <span class="icon"
              ><i class="fa-solid fa-file-circle-question"></i
            ></span>
            <span>Solicitudes</span>
          </a>
        </li>
        <li>
          <a href="#" v-on:click="cerrarSesion()">
            <span class="icon"
              ><i class="fa-solid fa-arrow-right-from-bracket"></i
            ></span>
            <span>Cerrar Sesión</span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    cerrarSesion() {
      this.$store.dispatch("userLogout").then(() => {
        this.$router.push({ name: "login" });
      });
    },
  },
};
</script>

<style></style>
