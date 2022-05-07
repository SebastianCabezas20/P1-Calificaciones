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
    
    print(Calificacion.objects.select_related('id_evaluacion').filter(id_evaluacion__nombre = "PEP2").all().query)
    coordinacion_seccions = Coordinacion_Seccion.objects.select_related('').filter().all()
     
    serializer = CoordinacionSeccionSerializer(coordinacion_seccions, many="true")
    return Response(serializer.data)