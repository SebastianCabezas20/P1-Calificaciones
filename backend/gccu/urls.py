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
from django.urls import path, re_path
from . import views

urlpatterns = [
    # URLs para obtener IDs de tipos de Usuarios.
    path('api/docente/<int:idUsuario>', views.getDocente),                              # Funcionando.
    path('api/jefeCarrera/<int:idUsuario>', views.getJefeCarrera),                      # Funcionando.
    path('api/coordinador/<int:idUsuario>', views.getCoordinador),
    path('api/estudiante/<int:idUsuario>', views.getIdEstudiante),                      # Funcionando.

    # Demás URLs
    path('add/solicitud', views.dataSolicitud),
    path('actualizar/solicitud/<int:idSolicitud>', views.dataSolicitud),
    path('solicitudes/<int:idUsuario>', views.dataSolicitud),
    path('calificacionesTeoria/<int:codigo>/<int:idUsuario>',views.getDataAsignatura),
    path('calificacionesLaboratorio/<int:codigo>/<int:idUsuario>',views.getDataAsignaturaLab),
    path('InformacionTeoria/<int:codigo>',views.getInformacionCursoTeoria),
    path('InformacionLaboratorio/<int:codigo>',views.getInformacionCursoLab),
    path('cursosEstudiante/<int:idUsuario>', views.getCursosByEstudiante),              # Funcionando.
    path('cursosDocente/<int:idUsuario>', views.getCursosByDocente),                    # Funcionando.
    path('estudiantes', views.getEstudiante), ### SIRVE?
    path('solicitudRespuesta/<int:idEstudiante>/<int:idEvaluacion>', views.getDataSolicitudRespuesta), ## Ver los datos de la respuesta a la apelacion
    path('actualizar/calificacion/<int:idCalificacion>', views.actualizacionCalificacionEstudiante), # Para poder actualizar calificaion de un estudiante 
    path('calificacion/coordinacion/<int:idCoordinacion>', views.getCalifiacionesEstudiantes),
    path('getCalificacionesPerAsignaturaEvaluacion/<int:idAsignatura>/<int:idEvaluacion>', views.getCalificacionesPerAsignaturaEvaluacion),
    path('asignaturascoordinador/<int:idCoordinador>', views.getAsignaturastoCoordinador),
    path('evaluaciones/<int:idCoordinacion>', views.evaluacionesCoordinacion),          # Funcionando.
    path('delete/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),       # Funcionando.
    path('add/evaluacion', views.evaluacionesCoordinacion),                             # Funcionando.
    path('evaluacion/<int:idEvaluacion>', views.crudOneEvaluacion),
    path('add/calificacion', views.calificacionesEstudiantes),                          
    path('evaluacion/tipos', views.getTiposEvaluaciones),
    path('coordinador/coordinacion/<int:idCoordinador>', views.getCoordinacionesCoordinador), # Saber la coordinacion que quiere revisar segun coordinador
    path('coordinaciones/asignatura/<int:idAsignatura>', views.getCoordinacionesAsignatura),
    path('coordinacion/solicitudes/<int:idCoordinacion>', views.getSolicitudesCurso), # Dada la coordinacion (seccion) mostrar sus solicitudes
    path('jefe/<int:idJefe>/asignaturas', views.getAsignaturasJefeCarrera), # Asignaturas segun jefe
    path('jefe/asignatura/solicitudes/<int:idAsignatura>', views.getSolicitudesAsignaturaJefeCarrera), # Apelaciones segun asignatura seleccionada por un jefe de carrera
    path('update/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),       # Funcionando. 
    path('allInfoEvaluaciones/<int:idCoordinacion>', views.getAllEvaluaciones),
    path('usuario/roles', views.getRolesUsuarios),                                      # Funcionando.
    path('authUser', views.isRolUser),                                                  # Funcionando.
    path('solicitudesDocente/<int:idDocente>', views.getSolicitudesByIdDocente),        # Funcionando.
    path('informacion/solicitud/estudiante/<int:idCalificacion>', views.getDataSolicitudApelacion),  
    path('calificacionesDocente/<int:idEvaluacion>', views.getCalificaionesByDocente),
    path('updateCalificacion/<int:idCalificacion>', views.updateCalificacion),
    path('add/cambio/calificacion',views.addCambioNota),
    path('get/cambio/calificacion/asignatura/<int:idAsignatura>',views.getCambioNota_idAsignatura),
    path('add/cambioFecha', views.cambioFechaCalificacion), 
    path('get/cambiosFecha', views.getCambiosFecha),  ## Verificar si aun se necesita para el dashboard
    path('get/evaluaciones/<nombreEvaluacion>/asignatura/<int:idAsignatura>', views.getEvaluacionesPorNombre),
    path('get/cambiosNota', views.getCambiosNota),
    path('get/coordinacion/<int:idCoordinacion>', views.informacionCoordinacion),
    path('get/cambio/ponderacion/asignatura/<int:idAsignatura>',views.getCambioPonderaciones), ## Obtener los cambios de ponderacion de una asignatura
    path('get/cambio/fecha/asignatura/<int:idAsignatura>',views.getCambioFecha), ## Obtener los cambios de fecha de una asignatura
    path('get/cambio/calificacion/curso/<int:idCurso>',views.getCambioNotaCurso),
    path('get/evPendientesEntrega/<int:idDocente>', views.getEntregaPendienteEvaluacion),
]
