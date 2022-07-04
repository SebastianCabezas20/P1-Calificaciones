"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # URLs para obtener IDs de tipos de Usuarios.
    path('api/docente/<int:idUsuario>', views.getDocente),
    path('api/jefeCarrera/<int:idUsuario>', views.getJefeCarrera),
    path('api/coordinador/<int:idUsuario>', views.getCoordinador),
    path('api/estudiante/<int:idUsuario>', views.getIdEstudiante),

    # Demás URLs
    path('add/solicitud', views.dataSolicitud),
    path('actualizar/solicitud/<int:idSolicitud>', views.dataSolicitud),
    path('solicitudes/<int:idUsuario>', views.dataSolicitud),
    path('calificacionesTeoria/<int:codigo>/<int:idUsuario>',views.getDataAsignatura),
    path('calificacionesLaboratorio/<int:codigo>/<int:idUsuario>',views.getDataAsignaturaLab),
    path('get/calificaciones/estudiante/<int:idUsuario>', views.getCalificacionesEstudiante),
    path('cursosEstudiante/<int:idUsuario>', views.getCursosByEstudiante),
    path('cursosDocente/<int:idUsuario>', views.getCursosByDocente),
    path('solicitudRespuesta/<int:idEstudiante>/<int:idEvaluacion>', views.getDataSolicitudRespuesta),
    path('actualizar/calificacion/<int:idCalificacion>', views.actualizacionCalificacionEstudiante),
    path('calificacion/coordinacion/<int:idCoordinacion>', views.getCalifiacionesEstudiantes),
    path('evaluaciones/<int:idCoordinacion>', views.evaluacionesCoordinacion),
    path('delete/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),
    path('add/evaluacion', views.evaluacionesCoordinacion),
    path('evaluacion/<int:idEvaluacion>', views.crudOneEvaluacion),
    path('add/calificacion', views.calificacionesEstudiantes),                          
    path('evaluacion/tipos', views.getTiposEvaluaciones),
    path('coordinador/coordinacion/<int:idCoordinador>', views.getCoordinacionesCoordinador),
    path('coordinaciones/asignatura/<int:idAsignatura>', views.getCoordinacionesAsignatura),
    path('coordinacion/solicitudes/<int:idCoordinacion>', views.getSolicitudesCurso),
    path('jefe/<int:idJefe>/asignaturas', views.getAsignaturasJefeCarrera),
    path('jefe/asignatura/solicitudes/<int:idAsignatura>', views.getSolicitudesAsignaturaJefeCarrera),
    path('update/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),
    path('allInfoEvaluaciones/<int:idCoordinacion>', views.getAllEvaluaciones),
    path('usuario/roles', views.getRolesUsuarios),
    path('authUser', views.isRolUser),
    path('solicitudesDocente/<int:idDocente>', views.getSolicitudesByIdDocente),
    path('informacion/solicitud/estudiante/<int:idCalificacion>', views.getDataSolicitudApelacion),  
    path('calificacionesDocente/<int:idEvaluacion>', views.getCalificaionesByDocente),
    path('updateCalificacion/<int:idCalificacion>', views.updateCalificacion),
    path('add/cambio/calificacion',views.addCambioNota),    
    path('get/cambio/calificacion/asignatura/<int:idAsignatura>',views.getCambioNota_idAsignatura),
    path('add/cambioFecha', views.cambioFechaCalificacion),
    path('add/cambioPonderacion', views.addCambioPonderacion),
    path('get/evaluaciones/<nombreEvaluacion>/asignatura/<int:idAsignatura>', views.getEvaluacionesPorNombre),
    path('get/cambiosNota/<int:idCoordinador>', views.getCambiosNota),
    path('get/coordinacion/<int:idCoordinacion>', views.informacionCoordinacion),
    path('get/cambio/ponderacion/asignatura/<int:idAsignatura>',views.getCambioPonderaciones),
    path('get/cambio/fecha/asignatura/<int:idAsignatura>',views.getCambioFecha),
    path('get/cambio/calificacion/curso/<int:idCurso>',views.getCambioNotaCurso),
    path('get/evPendientesEntrega/<int:idDocente>', views.getEntregaPendienteEvaluacion),
    path('get/asignaturasAtrasadas', views.getAsignaturasAtrasadas),
    path('get/seccionesAsignaturaAtrasadas/<int:idAsignatura>', views.getSeccionesAsignaturaAtrasadas),
    path('get/allEvaluacionesMail', views.getAllEvaluacionesMail),
    path('get/infodashboardcoordinador/<int:idUsuario>', views.getInfoDashboardCoordinador),
    path('get/infodashboardestudiante/<int:idUsuario>', views.getInfoDashboardEstudiante),
    path('get/infodashboardjefecarrera/<int:idUsuario>', views.getInfoDashboardJefeCarrera),
    path('get/secciones/asignatura/<int:idAsignatura>', views.getSeccionesAsignaturaJefeCarrera),
    path('get/dash/solicitudes/<int:idJefeCarrera>', views.getSolicitudesDashboardJefeCarrera),
    path('get/dash/cambioNotas/<int:idJefeCarrera>', views.getCambioNotasDashboardJefeCarrera),
    path('get/dash/cambioFecha/<int:idJefeCarrera>', views.getCambioFechaDashboardJefeCarrera),
    path('get/dash/atrasos/<int:idJefeCarrera>', views.getAtrasosDashboardJefeCarrera),
    path('get/calificaciones/<int:codigoAsig>/all', views.getAllCalificacionesByCurso),
    
    # URLs para cursos espejos (Docente).
    path('evaluaciones/<int:idUsuario>/<str:bloqueHorario>/CE', views.evaluacionesCoordinacionCursosEspejo),
    path('get/coordinacion/<int:idUsuario>/<str:bloqueHorario>/CE', views.informacionCoordinacionCursoEspejo),
    path('calificacion/coordinacion/<str:bloqueHorario>/<int:idDocente>/CE', views.getCalificacionesEstudiantesCursosEspejo),
    path('evaluacion/<str:nombreEvaluacion>/<str:bloqueHorario>/<int:idDocente>/CE', views.crudOneEvaluacionCursosEspejo),
    path('calificacionesDocente/<str:nombreEvaluacion>/<str:bloqueHorario>/<int:idDocente>/CE', views.getCalificacionesByDocenteCursosEspejo),
    path('isEstudianteInscrito/<str:bloqueHorario>/<int:idDocente>/<str:componente>/<int:idEstudiante>', views.estudiantePertenece),

    # URLs para el usuario Autoridad (Vicedecano - SubDirector)
    path('get/infodashboardautoridadsub/<int:idAutoridad>', views.getInfoDashboardAutoridadSub),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
