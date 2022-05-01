import { createRouter, createWebHistory } from "vue-router";
import CalificacionesView from "../views/Estudiante/CalificacionesView.vue";
import LoginView from "../views/General/LoginView.vue"
import LogoutView from "../views/LogoutView.vue"
import HomeView from "../views/Otros/HomeView.vue";
import ApelacionesAutoView from "../views/Autoridad/ApelacionesAutoView.vue";
import RespuestaApelacionView from "../views/Docente/RespuestaApelacionView.vue";
import DashboardEstudiante from "../views/Estudiante/DashboardEstudiante.vue";
import EstudianteCursoSeleccionado from "../views/Estudiante/EstudianteCursoSeleccionado.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/logout",
      name: "logout",
      component: LogoutView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/Otros/AboutView.vue"),
    },
    {
      path: "/home",
      name: "homeEstudiante",
      component: DashboardEstudiante,
    },
    {
      path: "/calificaciones",
      name: "calificaciones",
      component: CalificacionesView,
    },
    {
      path: "/apelaciones/autoridad",
      name: "apelacionesAutoAutoridad",
      component: ApelacionesAutoView,
    },
    {
      path: "/apelaciones/respuesta",
      name: "responderApelacionDocente",
      component: RespuestaApelacionView,
    },
    {
      path: "/home/cursoseleccionado",
      name: "cursoseleccionado",
      component: EstudianteCursoSeleccionado,
    }
  ],
});

export default router;
