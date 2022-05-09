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
    path('solicitudRespuesta', views.getDataSolicitudRespuesta),
    path('actualizar/solicitud', views.actualizacionSolicitudRespuesta),
    path('actualizar/calificacion', views.actualizacionCalificacionEstudiante),
    path('calificacionesEstudiantes', views.getCalifiacionesEstudiantes),
    path('solicitudesDocente', views.getDataSolicitudesDocente),
    path('calificacionespercursodocente', views.getCalificacionesPerCursoDocente),
    path('coordinacion/evaluaciones', views.evaluacionesCoordinacion),
    path('delete/evaluacion/<int:idEvaluacion>', views.evaluacionesCoordinacion),
]
