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
from . import views

urlpatterns = [
    # URLs para obtener IDs de tipos de Usuarios.
    path('api/docente/<int:idUsuario>', views.getDocente),                              # Funcionando.
    path('api/jefeCarrera/<int:idUsuario>', views.getJefeCarrera),                      # Funcionando.
    path('api/coordinador/<int:idUsuario>', views.getCoordinador),                      # Funcionando.

    # Demás URLs
    path('calificacionesTeoria/<int:codigo>',views.getDataAsignatura),
    path('calificacionesLaboratorio/<int:codigo>',views.getDataAsignaturaLab),
    path('InformacionTeoria/<int:codigo>',views.getInformacionCursoTeoria),
    path('InformacionLaboratorio/<int:codigo>',views.getInformacionCursoLab),
    path('solicitudes/<int:idUsuario>', views.getDataSolicitud),                        # Funcionando.
    path('cursosEstudiante', views.getCursosByEstudiante),
    path('cursosDocente/<int:idUsuario>', views.getCursosByDocente),                    # Funcionando.
    path('estudiantes', views.getEstudiante),
    path('solicitudRespuesta/<int:idEstudiante>/<int:idEvaluacion>', views.getDataSolicitudRespuesta), ## Ver los datos de la respuesta a la apelacion
    path('actualizar/solicitud/<int:idSolicitud>', views.actualizacionSolicitudRespuesta), # Para poder actualizar respuesta y estado de una solicitud
    path('actualizar/calificacion/<int:idCalificacion>', views.actualizacionCalificacionEstudiante), # Para poder actualizar calificaion de un estudiante 
    path('calificacion/coordinacion/<int:idCoordinacion>', views.getCalifiacionesEstudiantes),
    path('solicitudesDocente', views.getDataSolicitudesDocente),
    path('getCalificacionesPerAsignaturaEvaluacion/<int:idAsignatura>/<int:idEvaluacion>', views.getCalificacionesPerAsignaturaEvaluacion),
    path('asignaturascoordinador/<int:idCoordinador>', views.getAsignaturastoCoordinador),
    path('evaluaciones/<int:idCoordinacion>', views.evaluacionesCoordinacion),          # Funcionando.
    path('delete/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),       # Funcionando.
    path('add/evaluacion', views.evaluacionesCoordinacion),                             # Funcionando.
    path('evaluacion/<int:idEvaluacion>', views.crudOneEvaluacion),
    path('add/calificacion', views.calificacionesEstudiantes),                          
    path('evaluacion/tipos', views.getTiposEvaluaciones),
    path('coordinador/coordinacion/<int:idCoordinador>', views.getCoordinacionesCoordinador), # Saber la coordinacion que quiere revisar segun coordinador
    path('coordinacion/solicitudes/<int:idCoordinacion>', views.getSolicitudesCurso), # Dada la coordinacion (seccion) mostrar sus solicitudes
    path('jefe/<int:idJefe>/asignaturas', views.getAsignaturasJefeCarrera), # Asignaturas segun jefe
    path('jefe/asignatura/solicitudes/<int:idAsignatura>', views.getSolicitudesAsignaturaJefeCarrera), # Apelaciones segun asignatura seleccionada por un jefe de carrera
    path('update/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),       # Funcionando. 
    path('allInfoEvaluaciones/<int:idCoordinacion>', views.getAllEvaluaciones),
    path('usuario/roles', views.getRolesUsuarios),                                      # Funcionando.
    path('authUser', views.isRolUser),                                               # Funcionando.
    path('solicitudesDocente/<int:idDocente>', views.getSolicitudesByIdDocente),
]
