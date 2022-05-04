import { createRouter, createWebHistory } from "vue-router";
import CalificacionesView from "../views/Estudiante/CalificacionesView.vue";
import LoginView from "../views/General/LoginView.vue"
import LogoutView from "../views/LogoutView.vue"
import HomeView from "../views/Otros/HomeView.vue";
import ApelacionesAutoView from "../views/Autoridad/ApelacionesAutoView.vue";
import RespuestaApelacionView from "../views/Docente/RespuestaApelacionView.vue";
import DashboardEstudiante from "../views/Estudiante/DashboardEstudiante.vue";
import CursosEstudiante from "../views/Estudiante/CursosEstudiante.vue";
import ListadoApelacionesEstudiante from "../views/Estudiante/ListadoApelacionesEstudiante.vue";
import EstudianteCursoSeleccionado from "../views/Estudiante/EstudianteCursoSeleccionado.vue";
import DashboardAutoridad from "../views/Autoridad/DashboardAutoridad.vue";
import CursosJCSubdirector from "../views/Autoridad/CursosJCSubdirector.vue";
import CursosVicedecano from "../views/Autoridad/CursosVicedecano.vue";
import RegCambiosSolicitudesVicedecano from "../views/Autoridad/RegCambiosSolicitudesVicedecano.vue";
import CoordinadorCursoSeleccionado from "../views/Autoridad/CoordinadorCursoSeleccionado.vue";
import SolicitudApelacion from "../views/Estudiante/SolicitudApelacion.vue";
import ListadoApelacionesDocente from "../views/Docente/ListadoApelacionesDocente.vue";
import DashboardDocente from "../views/Docente/DashboardDocente.vue";
import CursosDocente from "../views/Docente/CursosDocente.vue";
import DocenteCursoSeleccionado from "../views/Docente/DocenteCursoSeleccionado.vue";
import SubirCalificacionesDocente from "../views/Docente/SubirCalificacionesDocente.vue";
import ModificacionCalificacionesDocente from "../views/Docente/ModificacionCalificacionesDocente.vue";

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
      path: "/home/cursos",
      name: "cursosEstudiante",
      component: CursosEstudiante,
    },
    {
      path: "/home/calificaciones",
      name: "calificaciones",
      component: CalificacionesView,
    },
    {
      path: "/home/apelaciones",
      name: "ApelacionesEstudiante",
      component: ListadoApelacionesEstudiante,
    },
    {
      path: "/home/apelacion",
      name: "apelacion",
      component: SolicitudApelacion,
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
    },
    {
      path: "/homeAutoridad",
      name: "homeAutoridad",
      component: DashboardAutoridad,
    },
    {
      path: "/homeAutoridad/cursos",
      name: "cursosAutoridad",
      component: CursosJCSubdirector,
    },
    {
      path: "/homeAutoridad/cursosVicedecano",
      name: "cursosAutoridadVicedecano",
      component: CursosVicedecano,
    },
    {
      path: "/homeAutoridad/registrovicedecano",
      name: "registroVicedecano",
      component: RegCambiosSolicitudesVicedecano,
    },
    {
      path: "/homeAutoridad/cursoseleccionadoCoordinador",
      name: "cursoSeleccionadoCoordinador",
      component: CoordinadorCursoSeleccionado,
    },
    {
      path: "/homedocente",
      name: "homeDocente",
      component: DashboardDocente,
    },
    {
      path: "/homedocente/cursos",
      name: "cursosDocente",
      component: CursosDocente,
    },
    {
      path: "/homedocente/cursoseleccionado",
      name: "cursoSeleccionadoDocente",
      component: DocenteCursoSeleccionado,
    },
    {
      path: "/homedocente/subircalificaciones",
      name: "cursosubircalificaciones",
      component: SubirCalificacionesDocente,
    },
    {
      path: "/homedocente/modificacioncalificaciones",
      name: "cursomodificarcalificaciones",
      component: ModificacionCalificacionesDocente,
    },
    {
      path: "/homedocente/apelaciones",
      name: "Apelacionesdocente",
      component: ListadoApelacionesDocente,
    }
  ],
});

export default router;
