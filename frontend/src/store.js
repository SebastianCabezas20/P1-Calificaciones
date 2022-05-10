import { createStore } from "vuex";
import { getAPI } from "./axios-api";

const store = createStore({
  state: {
    idUsuario: null,
    nombreUsuario: "",
    nombre: "",
    apellido: "",
    email: "",
    idRol: null,
  },

  mutations: {
    updateUser(state, { idUsario, nombreUsuario, nombre, apellido, email, idRol }) {
      state.idUsuario = idUsario;
      state.nombreUsuario = nombreUsuario;
      state.nombre = nombre;
      state.apellido = apellido;
      state.email = email;
      state.idRol = idRol;
    },
  },
  actions: {
    userLogin(context, usercredential) {
      return new Promise((resolve, reject) => {
        // Primera comprobación: Nombre de usuario y contraseña coinciden con un usuario.
        getAPI
          .post("api/token/", {
            username: usercredential.nombreUsuario,
            password: usercredential.password,
          })
          .then((response) => {
            // Segunda comprobación: El usuario tiene el rol indicado en el select list.
            getAPI
              .post("authUser", {
                nombreUsuario: usercredential.nombreUsuario,
                idRolSeleccionado: usercredential.idRolSeleccionado,
              })
              .then(function (response2) {
                  console.log(response2.data)
                context.commit("updateUser", {
                  idUsuario: response2.data.id,
                  nombreUsuario: response2.data.username,
                  nombre: response2.data.first_name,
                  apellido: response2.data.last_name,
                  email: response2.data.email,
                  idRol: usercredential.idRolSeleccionado
                });
                localStorage.setItem("accessToken", response.data.access);
                resolve();
              })
              .catch(function (err) {
                  reject(err);
              });
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
  },
  getters: {
      infoUser(state){
        // solo prueba de que funciona.  
        let algo = {
              a: state.idUsuario,
                b: state.idRol
          }
          return algo;
      }
  }
});

export default store;
