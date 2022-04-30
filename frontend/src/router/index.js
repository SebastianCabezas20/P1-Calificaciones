import { createRouter, createWebHistory } from "vue-router";
import CalificacionesView from "../views/CalificacionesView.vue";
import LoginView from "../views/LoginView.vue"
import LogoutView from "../views/LogoutView.vue"
import HomeView from "../views/HomeView.vue";
import ApelacionesAutoView from "../views/ApelacionesAutoView.vue";
import RespuestaApelacionView from "../views/RespuestaApelacionView.vue";
import DashboardEstudiante from "../views/DashboardEstudiante.vue";

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
      component: () => import("../views/AboutView.vue"),
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
      name: "apelacionesAuto",
      component: ApelacionesAutoView,
    },
    {
      path: "/apelaciones/respuesta",
      name: "respuestaApelacion",
      component: RespuestaApelacionView,
    },
  ],
});

export default router;
