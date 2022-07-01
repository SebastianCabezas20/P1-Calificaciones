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
          <a href="/autoridad/home">
            <span class="icon"><i class="fa-solid fa-house"></i></span>
            <span>Inicio</span>
          </a>
        </li>
        <!--
        <li>
          <a href="/jefe/asignaturas/general">
            <span class="icon"><i class="fa-solid fa-book"></i></span>
            <span>Cambio de notas</span>
          </a>
        </li>
        <li>
          <a href="/jefe/asignaturas/cambio/ponderacion">
            <span class="icon"><i class="fa-solid fa-book"></i></span>
            <span>Cambio de ponderaciones</span>
          </a>
        </li>
        <li>
          <a href="/jefe/asignaturas/cambio/fecha">
            <span class="icon"><i class="fa-solid fa-book"></i></span>
            <span>Cambio de fechas</span>
          </a>
        </li>
        <li>
          <a href="/jefe/asignaturas">
            <span class="icon"
              ><i class="fa-solid fa-file-circle-question"></i
            ></span>
            <span>Solicitudes</span>
          </a>
        </li>
        <li>
          <a href="/jefe/asignaturasAtrasos">
            <span class="icon"
              ><i class="fa-solid fa-file-circle-question"></i
            ></span>
            <span>Atrasos</span>
          </a>
        </li>
        -->
        <li>
          <a href="#" v-on:click="cerrarSesion()">
            <span class="icon"
              ><i class="fa-solid fa-arrow-right-from-bracket"></i
            ></span>
            <span>Cerrar sesión</span>
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
