<template>
  <div>
    <NavbarLogin></NavbarLogin>

    <div id="contentLogin">
      <div id="formDeLogin">
        <div id="cabeceraLogin">
          <img
            src="../../assets/Logo_usach.png"
            id="logoLogin"
            alt="Logo Usach"
          />
          <h1>Intranet</h1>
          <h2>Facultad de Ingeniería</h2>
        </div>

        <form action="#" method="POST" v-on:submit.prevent="login">
          <div class="px-5 pt-2">
            <label for="username" class="sr-only">Nombre de Usuario</label>
            <input
              type="text"
              name="username"
              id="username"
              v-model="username"
              placeholder="Usuario sin @usach.cl"
              required
              class="textLogin"
            />
          </div>

          <div class="px-5 pt-2">
            <label for="password" class="sr-only">Contraseña</label>
            <input
              type="password"
              name="password"
              id="pass"
              v-model="password"
              placeholder="Contraseña"
              required
              class="textLogin"
            />
          </div>

          <div class="flex justify-center px-5 pt-2">
            <div>
              <select
                class="form-select appearance-none block w-full px-3 py-1.5 text-gray-900 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded-lg transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-azul-usach focus:outline-none"
                v-model="rol"
              >
                <option v-for="opcion in opciones" v-bind:value="opcion.value">
                  {{ opcion.text }}
                </option>
              </select>
            </div>
          </div>

          <div class="px-5" v-if="incorrectAuth">
            <div id="incorrectCredentials">
              <p>Rut o contraseña incorrecta. Intente nuevamente</p>
            </div>
          </div>

          <div class="px-5 pt-3 d-flex justify-content-center">
            <button
              type="submit"
              class="btn btn-primary relative justify-center py-2 px-4"
            >
              Enviar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarLogin from "../../components/NavbarLogin.vue";

export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      rol: null,
      opciones: [
        { value: null, text: "Seleccione un rol" },
        { value: "Estudiante", text: "Estudiante" },
        { value: "Docente", text: "Docente" },
        { value: "Coordinador", text: "Coordinador" },
        { value: "Jefe_Carrera", text: "Jefe de Carrera" },
        { value: "Subdirector_Docente", text: "Subdirector Docente" },
        { value: "Vicedecano_Docencia", text: "Vicedecano de Docencia" },
      ],
      incorrectAuth: false,
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "homeEstudiante" });
        })
        .catch((err) => {
          this.incorrectAuth = true;
        });
    },
  },

  components: {
    NavbarLogin,
  },
};
</script>

<style>
#contentLogin {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

#formDeLogin {
  width: 30%;
  height: 100%;
  border: 1px solid #004883;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  padding: 20px;
}

#logoLogin {
  height: 300px;
  width: 300px;
}

#cabeceraLogin {
  text-align: center;
}

#cabeceraLogin h1 {
  font-weight: bold;
  font-size: 1000;
  margin-top: 10px;
}

#cabeceraLogin h2 {
  font-weight: bold;
  font-size: 900;
  margin-top: 5px;
}

.textLogin {
  position: relative;
  display: block;
  width: 100%;
  padding: 5px 10px;
  border: 1px solid #004883;
  border-radius: 5px;
}

#incorrectCredentials {
  background-color: red;
  color: white;
  position: relative;
  display: block;
  font-size: 600;
  padding: 2px 3px;
  border: 1px solid white;
}
</style>
