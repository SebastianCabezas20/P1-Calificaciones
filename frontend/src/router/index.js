import { createRouter, createWebHistory } from "vue-router";
import CalificacionesView from "../views/Estudiante/CalificacionesView.vue";
import LoginView from "../views/General/LoginView.vue";
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
import JefeAsignaturasGeneralVue from "../views/Autoridad/JefeAsignaturasGeneral.vue";
import DashboardCoordinador from "../views/Autoridad/DashboardCoordinador.vue"
import DashboardJefeCarrera from "../views/Autoridad/DashboardJefeCarrera.vue"
import AsignaturasJefeCambiosVue from "../views/Autoridad/AsignaturasJefeCambios.vue";
import JefeAsignaturaCambioPonderacionVue from "../views/Autoridad/JefeAsignaturaCambioPonderacion.vue";
import CambioPonderacionJefeVue from "../views/Autoridad/CambioPonderacionJefe.vue";
import JefeAsignaturaCambioFechaVue from "../views/Autoridad/JefeAsignaturaCambioFecha.vue";
import CambiosFechaJefeVue from "../views/Autoridad/CambiosFechaJefe.vue";
import CoordinadorSeccionCambioNotasVue from "../views/Autoridad/CoordinadorSeccionCambioNotas.vue";
import CambioNotasCoordinador from "../views/Autoridad/CambioNotasCoordinador.vue";
import SubirCalificacionesCoordinador from "../views/Autoridad/SubirCalificacionesCoordinador.vue";
import atrasosJefeVue from "../views/Autoridad/atrasosJefeCarrera.vue";

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
      path: "/estudiante/calificaciones/:codigoAsignatura",
      name: "calificaciones",
      component: CalificacionesView,
      props: true,
    },
    {
      path: "/estudiante/apelaciones",
      name: "ApelacionesEstudiante",
      component: ListadoApelacionesEstudiante,
    },
    {
      path: "/estudiante/add/solicitud/:idCalificacion",
      name: "apelacion",
      component: SolicitudApelacion,
      props: true,
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
      props: true,
    },
    {
      // Formulario para contestar solicitudes
      path: "/docente/apelacion/answer/:idEstudiante/:idEvaluacion",
      name: "responderApelacionDocente",
      component: RespuestaApelacionView,
      props: true,
    },
    {
      path: "/docente/curso/:idCurso/add/calificacion/:idEvaluacion",
      name: "cursosubircalificaciones",
      component: SubirCalificacionesDocente,
      props: true,
    },
    {
      path: "/docente/curso/:idCurso/evaluacion/:idEvaluacion",
      name: "cursoSeleccionadoDocente2",
      component: ModificacionCalificacionesDocente,
      props: true,
    },
    {
      /// Solicitudes de un docente
      path: "/docente/solicitudes",
      name: "Apelacionesdocente",
      component: ListadoApelacionesDocente,
    },

    // Vistas de Autoridades

    // COORDINADOR
    {
      path: "/coordinador/home",
      name: "homeCoordinador",
      component: DashboardCoordinador,
    },
    // Secciones de un coordinador para uso general
    {
      path: "/coordinador/asignaturas/general",
      name: "asignaturasCoordinador",
      component: AsignaturasCoordinador,
    },  
    // Secciones de un coordinador para solicitudes
    { 
      path: "/coordinador/seccion",
      name: "seccionesCoordinador",
      component: CoordinadorSecciones,
    },
    //Solicitudes segun coordinacion-curso de un coordinador
    {
      path: "/coordinador/seccion/solicitudes/:idCurso",
      name: "solicitudesSeccionCoordinador",
      component: CoordinadorSolicitudesCurso,
      props: true,
    },
    { // Mostrar algo de un curso seleccionado
      path: "/coordinador/asignatura/:idAsignatura/seccion/:idCurso",
      name: "seccionSeleccionadaCoordinador",
      component: CoordinadorCursoSeleccionado,
      props: true,
    },
    { //Calificacion de una evaluacion por parte de un coordinador
      path: "/coordinador/curso/:idCurso/add/calificacion/:idEvaluacion",
      name: "cursosubircalificacionescoordinador",
      component: SubirCalificacionesCoordinador,
      props: true,
    },
    // Secciones de un coordinador para visualizar cambio de calificaciones
    {
      path: "/coordinador/cursos/cambio/calificacion",
      name: "asignaturasCooordinadorCambioNotas",
      component: CoordinadorSeccionCambioNotasVue,
    },  
    { // Mostrar cambio de califiaciones segun curso/seccion selecionado
      path: "/coordinador/curso/:idCurso/cambio/calificacion",
      name: "seccionSeleccionadaCoordinadorCambioNotas",
      component: CambioNotasCoordinador,
      props: true,
    },
    {
      path: "/autoridad/home",
      name: "homeAutoridad",
      component: DashboardAutoridad,
    },
    {
      path: "/jefeCarrera/home",
      name: "homeJefeCarrera",
      component: DashboardJefeCarrera,
    },
    {
      path: "/autoridad/solicitudes",
      name: "apelacionesAutoAutoridad",
      component: ApelacionesAutoView,
    },
    { //Asignaturas de un jefe de carrera solicitudes
      path: "/jefe/asignaturas",
      name: "asignaturasJefeDeCarreraGeneral",
      component: JefeAsignaturasApe,
    },
    { //Asignaturas de un jefe de carrera general para cambio de notas
      path: "/jefe/asignaturas/general",
      name: "asignaturasJefeDeCarrera",
      component: JefeAsignaturasGeneralVue,
    },
    { //Apelaciones para un jefe de carrera segun asignatura
      path: "/jefe/asignaturas/apelaciones/:idAsignatura",
      name: "apelacionesAsignaturasJefeDeCarrera",
      component: JefeApelacionesAsig,
      props: true,
    },
    { // Mostrar los cambios de nota segun asignatura de jefe de carrera
      path: "/jefe/asignaturas/cambios/nota/:idAsignatura",
      name: "cambiosAsignaturasJefeDeCarrera",
      component: AsignaturasJefeCambiosVue,
      props: true,
    },
    { // Mostrar las asignatura de jefe de carrera para mostrar cambios de ponderacion
      path: "/jefe/asignaturas/cambio/ponderacion",
      name: "AsignaturasCambioPonderacion",
      component: JefeAsignaturaCambioPonderacionVue,
    },
    { // Mostrar los cambios de ponderacion segun asignatura de jefe de carrera
      path: "/jefe/asignaturas/cambios/ponderacion/:idAsignatura",
      name: "cambiosPonderacionJefeCarrera",
      component: CambioPonderacionJefeVue,
      props: true,
    },
    { // Mostrar las asignatura de jefe de carrera para mostrar cambios de fecha
      path: "/jefe/asignaturas/cambio/fecha",
      name: "AsignaturasCambioFecha",
      component: JefeAsignaturaCambioFechaVue,
    },
    { // Mostrar los cambios de fecha segun asignatura de jefe de carrera
      path: "/jefe/asignaturas/cambios/fecha/:idAsignatura",
      name: "cambiosFechaJefeCarrera",
      component: CambiosFechaJefeVue,
      props: true,
    },
    { // Mostrar los Atrasos en entrega segun asignatura de jefe de carrera
      path: "/jefe/asignaturasAtrasos",
      name: "atrasosJefeCarrera",
      component: atrasosJefeVue,
      props: true,
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
    
  ],
});

export default router;
