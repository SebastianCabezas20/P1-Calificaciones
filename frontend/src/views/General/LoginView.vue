<template>
  <div>
    <NavbarLogin></NavbarLogin>

    <div id="contentLogin">
      <div id="formDeLogin">
        <div id="cabeceraLogin">
          <img
            src="../../assets/Logo_Usach.png"
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
              :type="tipoPassword"
              name="password"
              id="pass"
              v-model="password"
              placeholder="Contraseña"
              required
              class="textLogin"
            />
            <span
              class="fa-regular fa-eye algo"
              id="eyeLogin"
              @click="cambioCampo()"
            ></span>
          </div>

          <div class="flex justify-center px-5 pt-2">
            <div>
              <select
                class="form-select appearance-none block w-full px-3 py-1.5 text-gray-900 border border-solid border-gray-300 rounded-lg transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-azul-usach focus:outline-none"
                v-model="rolSeleccionado"
                required
              >
                <option selected disabled>Seleccione su tipo de usuario</option>
                <option v-for="rol in roles" v-bind:value="rol.id">
                  {{ rol.name }}
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
              type=""
              class="btn btn-primary relative justify-center py-2 px-4"
              @click.prevent="login()"
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
import axios from "axios";
import emailjs from 'emailjs-com';
import moment from 'moment';

export default {
  components: {
    NavbarLogin,
  },
  data() {
    return {
      username: "",
      password: "",
      rolSeleccionado: null,
      roles: [],
      incorrectAuth: false,
      tipoPassword: "password",
      evaluaciones: [],
      fechaEval: moment(),
      fechaFormat: moment(),
      hoy: moment(),
      dif: moment(),
    };
  },
  methods: {
    login() {
      /*for (var i = 0; i < this.evaluaciones.length; i++) {
        if (this.username == this.evaluaciones[i].id_docente.id_usuario.username) {
          var fechaEval = this.evaluaciones[i].fechaEntrega;
          var fechaEvalFormat = moment(fechaEval);
          console.log(fechaEvalFormat)
          var hoy = moment();
          console.log(hoy)
          var dif = fechaEvalFormat.diff(hoy, 'days');
          console.log(dif)
          if (dif <= 4 && dif >= 0) {
            console.log(this.evaluaciones[i].id_docente.id_usuario.email);
            emailjs.send('pingeso', 'template_evaluacion', {
              mail_mail: this.evaluaciones[i].id_docente.id_usuario.email,
              mail_evaluacion: this.evaluaciones[i].nombre,
              mail_docente: (this.evaluaciones[i].id_docente.id_usuario.first_name)+' '+(this.evaluaciones[i].id_docente.id_usuario.last_name),
              mail_fecha: this.evaluaciones[i].fechaEntrega,
              mail_asignatura: this.evaluaciones[i].id_coordinacion.id_asignatura.nombre
            },
            'TIAwArj4Go2oOAbqv')
            .then(function(response) {
              console.log('SUCCESS!', response.status, response.text);
            }, function(error) {
              console.log('FAILED...', error);
            });
          }
        }
      }*/
      this.$store
        .dispatch("userLogin", {
          nombreUsuario: this.username,
          password: this.password,
          idRolSeleccionado: this.rolSeleccionado,
        })
        .then(() => {
          if (this.$store.getters.idRolUsuario == 1)
            this.$router.push({ name: "homeEstudiante" });
          else if (this.$store.getters.idRolUsuario == 2)
            this.$router.push({ name: "homeDocente" });
          else if (this.$store.getters.idRolUsuario == 3)
            this.$router.push({ name: "homeCoordinador" });
          else if (this.$store.getters.idRolUsuario == 4)
            this.$router.push({ name: "homeJefeCarrera" });
          else this.$router.push({ name: "homeAutoridad" });
        })
        .catch((err) => {
          this.incorrectAuth = true;
        });
    },
    cambioCampo() {
      if (this.tipoPassword == "password") {
        this.tipoPassword = "text";
      } else {
        this.tipoPassword = "password";
      }
    },
  },
  mounted() {
    let that = this;
    axios.get("http://localhost:8000/usuario/roles").then(function (response) {
      that.roles = response.data;
    });
    axios.get("http://localhost:8000/get/allEvaluacionesMail").then(function (response) {
      that.evaluaciones = response.data;
    });
  },
};
</script>

<style></style>
