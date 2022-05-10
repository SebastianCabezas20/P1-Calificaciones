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
    path('calificacionesTeoria',views.getDataAsignatura),
    path('calificacionesLaboratorio',views.getDataAsignaturaLab),
    path('solicitudes', views.getDataSolicitud),
    path('cursosEstudiante', views.getCursosByEstudiante),
    path('cursosDocente', views.getCursosByDocente),
    path('estudiantes', views.getEstudiante),
    path('prueba', views.prueba),
    path('solicitudRespuesta', views.getDataSolicitudRespuesta), ## Ver los datos de la respuesta a la apelacion
    path('actualizar/solicitud', views.actualizacionSolicitudRespuesta), # Para poder actualizar respuesta y estado de una solicitud
    path('actualizar/calificacion', views.actualizacionCalificacionEstudiante), # Para poder actualizar calificaion de un estudiante 
    path('calificacionesEstudiantes', views.getCalifiacionesEstudiantes),
<<<<<<< Updated upstream
    path('solicitudesDocente', views.getDataSolicitudesDocente),
    path('calificacionespercursodocente', views.getCalificacionesPerCursoDocente),
    path('coordinacion/evaluaciones', views.evaluacionesCoordinacion),
    path('delete/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),
    path('evaluacion/tipos', views.getTiposEvaluaciones),
=======
    path('coordinador/coordinacion', views.getCoordinacionesCoordinador), # Saber la coordinacion que quiere revisar
    path('coordinacion/solicitudes', views.getSolicitudesCurso), # Dada la coordinacion mostrar sus solicitudes
    path('jefe/planes', views.getAsignaturasJefeCarrera), # Asignaturas segun jefe
    path('jefe/planes', views.getAsignaturasJefeCarrera), # 
>>>>>>> Stashed changes
]
