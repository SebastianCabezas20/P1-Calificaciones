from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def getData(request):
    calificaciones = Calificacion.objects.all()
    serializer = CalificacionSerializer(calificaciones, many="true")
    return Response(serializer.data)
