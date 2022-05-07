from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def getData(request):
    
    print(Calificacion.objects.select_related('id_evaluacion').filter(id_evaluacion__nombre = "PEP2").all().query)
    calificaciones = Calificacion.objects.select_related('id_evaluacion').filter().all()
    
    for calificacion in calificaciones:
        print(calificacion.id_evaluacion.nombre)
    
 
    serializer = CalificacionSerializer(calificaciones, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getDataAsignatura(request):
    
    print(Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = '10110').all().query)
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = "10110", id_evaluacion__id_coordinacion__id_asignatura__componente = "T", id_estudiante__id = "1").all()
    serializer = CalificacionSerializer(calificaciones, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getDataAsignaturaLab(request):
    
    print(Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = '10110').all().query)
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = "10110", id_evaluacion__id_coordinacion__id_asignatura__componente = "L", id_estudiante__id = "1").all()
    serializer = CalificacionSerializer(calificaciones, many="true")
    print(Calificacion.objects.select_related('id_evaluacion').filter(id_evaluacion__nombre = "PEP2").all().query)
    coordinacion_seccions = Coordinacion_Seccion.objects.select_related('').filter().all()
     
    serializer = CoordinacionSeccionSerializer(coordinacion_seccions, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getDataSolicitud(request):
    print(Solicitud_Revision.objects.select_related('id_estudiante').filter(id_estudiante__id = 2).all().query)
    solicitudes = Solicitud_Revision.objects.select_related('id_estudiante').filter(id_estudiante__id = 2).all()

    serializer = SolicitudSerializer(solicitudes, many = "true")
    return Response(serializer.data)