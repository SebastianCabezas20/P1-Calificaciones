import { createRouter, createWebHistory } from "vue-router";
import CalificacionesView from "../views/Estudiante/CalificacionesView.vue";
import LoginView from "../views/General/LoginView.vue";
import LogoutView from "../views/LogoutView.vue";
import HomeView from "../views/Otros/HomeView.vue";
import ApelacionesAutoView from "../views/Autoridad/ApelacionesAutoView.vue";
import RespuestaApelacionView from "../views/Docente/RespuestaApelacionView.vue";
import DashboardEstudiante from "../views/Estudiante/DashboardEstudiante.vue";
import CursosEstudiante from "../views/Estudiante/CursosEstudiante.vue";
import ListadoApelacionesEstudiante from "../views/Estudiante/ListadoApelacionesEstudiante.vue";
import EstudianteCursoSeleccionado from "../views/Estudiante/EstudianteCursoSeleccionado.vue";
import DashboardAutoridad from "../views/Autoridad/DashboardAutoridad.vue";
import AsignaturasCoordinador from "../views/Autoridad/AsignaturasCoordinador.vue";
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
import CoordinadorSecciones from "../views/Autoridad/CoordinadorSecciones.vue";
import CoordinadorSolicitudesCurso from "../views/Autoridad/CoordinadorSolicitudesCurso.vue";
import JefeAsignaturasApe from "../views/Autoridad/JefeAsignaturasApe.vue";
import JefeApelacionesAsig from "../views/Autoridad/JefeApelacionesAsig.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Vistas Generales
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

    // Vistas de Estudiantes
    {
      path: "/estudiante/home",
      name: "homeEstudiante",
      component: DashboardEstudiante,
    },
    {
      path: "/estudiante/cursos",
      name: "cursosEstudiante",
      component: CursosEstudiante,
    },
    {
      path: "/estudiante/calificaciones",
      name: "calificaciones",
      component: CalificacionesView,
    },
    {
      path: "/estudiante/apelaciones",
      name: "ApelacionesEstudiante",
      component: ListadoApelacionesEstudiante,
    },
    {
      path: "/estudiante/add/solicitud",
      name: "apelacion",
      component: SolicitudApelacion,
    },
    {
      path: "/estudiante/curso",
      name: "cursoseleccionado",
      component: EstudianteCursoSeleccionado,
    },

    // Vistas de Docentes
    {
      path: "/docente/home",
      name: "homeDocente",
      component: DashboardDocente,
    },
    {
      path: "/docente/cursos",
      name: "cursosDocente",
      component: CursosDocente,
    },
    {
      path: "/docente/curso/:idCurso",
      name: "cursoSeleccionadoDocente",
      component: DocenteCursoSeleccionado,
      props: true
    },
    {
      path: "/docente/apelacion/answer",
      name: "responderApelacionDocente",
      component: RespuestaApelacionView,
    },
    {
      path: "/docente/add/calificacion",
      name: "cursosubircalificaciones",
      component: SubirCalificacionesDocente,
    },
    {
      path: "/docente/modify/calificacion",
      name: "cursomodificarcalificaciones",
      component: ModificacionCalificacionesDocente,
    },
    {
      path: "/docente/solicitudes",
      name: "Apelacionesdocente",
      component: ListadoApelacionesDocente,
    },

    // Vistas de Autoridades
    {
      path: "/autoridad/home",
      name: "homeAutoridad",
      component: DashboardAutoridad,
    },    
    {
      path: "/autoridad/solicitudes",
      name: "apelacionesAutoAutoridad",
      component: ApelacionesAutoView,
    }, 
    {
      path: "/coordinador/seccion",
      name: "seccionesCoordinador",
      component: CoordinadorSecciones,
    }, 
    { //Solicitudes segun coordinacion-curso de un coordinador
      path: "/coordinador/seccion/solicitudes/:idCurso",
      name: "solicitudesSeccionCoordinador",
      component: CoordinadorSolicitudesCurso,
      props: true
    },
    { //Asignaturas de un jefe de carrera
      path: "/jefe/asignaturas",
      name: "asignaturasJefeDeCarrera",
      component: JefeAsignaturasApe,
    },
    { //Apelaciones para un jefe de carrera segun asignatura
      path: "/jefe/asignaturas/apelaciones/:idAsignatura",
      name: "apelacionesAsignaturasJefeDeCarrera",
      component: JefeApelacionesAsig,
      props: true
    },
    {
      path: "/autoridad/asignaturas",
      name: "cursosAutoridad",
      component: CursosJCSubdirector,
    },
    {
      path: "/autoridad/cursosVicedecano",
      name: "cursosAutoridadVicedecano",
      component: CursosVicedecano,
    },
    {
      path: "/autoridad/registros",
      name: "registroVicedecano",
      component: RegCambiosSolicitudesVicedecano,
    },
    {
      path: "/autoridad/asignatura",
      name: "cursoSeleccionadoCoordinador",
      component: CoordinadorCursoSeleccionado,
    },
    {
      path: "/autoridad/coordinador/asignaturas",
      name: "asignaturasCoordinador",
      component: AsignaturasCoordinador,
    },
  ],
});

export default router;
