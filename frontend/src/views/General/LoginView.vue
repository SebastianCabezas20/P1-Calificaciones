<template>
  <div class="login-form font-Inter">
    <NavbarLogin></NavbarLogin>

    <div class="min-h-full flex item-center justify-center py-20">
      <div
        class="max-w-lg w-full space-y-10 rounded-lg border-2 border-gris-usach shadow-xl"
      >
        <div>
          <img
            src="../assets/Logo_usach.png"
            class="mx-auto h-52 w-auto pt-5"
            alt="Logo Usach"
          />
          <h1 class="text-center text-3xl font-bold mt-5">Intranet</h1>
          <h2 class="text-center text-xl">Facultad de Ingeniería</h2>
        </div>

        <div v-if="incorrectAuth">
            <p class="text-center">Rut o contraseña incorrecta. Intente nuevamente</p>
        </div>

        <form class="mt-4 space-y-8 pb-5" action="#" method="POST" v-on:submit.prevent="login">
          <div class="px-5">
            <label for="rut" class="sr-only">Rut</label>
            <input
              type="text"
              name="rut"
              id="rut"
              v-model="rut"
              placeholder="Rut"
              required
              class="relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-lg focus:outline-none focus:ring-azul-usach focus:border-azul-usach focus:z-10 sm:text-md"
            />
          </div>

          <div class="px-5">
            <label for="password" class="sr-only">Contraseña</label>
            <input
              type="password"
              name="password"
              id="pass"
              v-model="password"
              placeholder="Contraseña"
              required
              class="relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-lg focus:outline-none focus:ring-azul-usach focus:border-azul-usach focus:z-10 sm:text-md"
            />
          </div>

          <div class="flex justify-center px-5">
            <div class="w-full">
              <select class="form-select appearance-none
                block
                w-full
                px-3
                py-1.5
                text-gray-900
                bg-white bg-clip-padding bg-no-repeat
                border border-solid border-gray-300
                rounded-lg
                transition
                ease-in-out
                m-0
                focus:text-gray-700 focus:bg-white focus:border-azul-usach focus:outline-none" v-model="rol">
                  <option v-for="opcion in opciones" v-bind:value="opcion.value">
                    {{ opcion.text }}
                  </option>
              </select>
            </div>
          </div>

          <div class="px-5">
            <button
              type="submit"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-md font-medium rounded-lg text-white bg-azul-usach hover:bg-azulHoverUsach focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
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
    name: 'login',
    data() {
        return {
            rut: '',
            password: '',
            rol: null,
            opciones: [
                {value: null, text: 'Seleccione un rol'},
                {value: 'Estudiante', text: 'Estudiante'},
                {value: 'Docente', text: 'Docente'},
                {value: 'Coordinador', text: 'Coordinador'},
                {value: 'Jefe_Carrera', text: 'Jefe de Carrera'},
                {value: 'Subdirector_Docente', text: 'Subdirector Docente'},
                {value: 'Vicedecano_Docencia', text: 'Vicedecano de Docencia'},
            ],
            incorrectAuth: false
        }
    },
    methods: {
        login() {
            this.$store.dispatch('userLogin', {
                rut: this.rut,
                password: this.password,
                rol: this.rol
            })
            .then(() => {
                this.$router.push({ name: 'calificaciones' })
            })
            .catch(err => {
                console.log(err)
                this.incorrectAuth = true
            })
        }
    },
  
    components: {
        NavbarLogin,
    },
};
</script>

<style></style>
