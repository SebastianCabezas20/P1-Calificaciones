<template>
  <head>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    />
  </head>

  <body>
    <div class="wrapper">
      <div class="sidebar">
        <div class="logo">
          <div>
            <img src="../assets/Usach-Trans.png" alt="Logo Usach" />
          </div>
        </div>

        <div class="linkSidebar">
          <ul>
            <li>
              <a href="#">
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
              <a href="#">
                <span class="icon"><i class="fa-solid fa-book"></i></span>
                <span>Mis Cursos</span>
              </a>
            </li>
            <li>
              <a href="#">
                <span class="icon"
                  ><i class="fa-solid fa-file-circle-question"></i
                ></span>
                <span>Solicitudes</span>
              </a>
            </li>
            <li>
              <a href="#">
                <span class="icon"
                  ><i class="fa-solid fa-arrow-right-from-bracket"></i
                ></span>
                <span>Cerrar Sesión</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
export default {};
</script>

<style>
.wrapper .sidebar {
  background-color: #004883;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 260px;
  padding: 3px;
  transition: all 0.5s ease;
  z-index: 1;
}

.wrapper .sidebar .logo {
  margin-bottom: 30px;
}

.wrapper .sidebar .logo img {
  display: block;
  margin: 0 auto;
}

.wrapper .sidebar ul li a {
  display: block;
  position: relative;
  font-size: 18px;
  font-weight: bold;
  padding: 15px 0px;
  color: white;
  text-decoration: none;
  font-family: "Inter", sans-serif;
}

.linkSidebar{
  display: flex;
  justify-content: center;
  align-items: center;
}

.wrapper .sidebar ul li a .icon {
  color: white;
  display: inline-block;
  width: 50px;
}

.wrapper .sidebar ul li a:hover,
.wrapper .sidebar ul li a:active {
  background-color: #0259a0;
}
</style>
