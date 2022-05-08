from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura      
        fields = '__all__'  

class CoordinacionSeccionSerializer(serializers.ModelSerializer):
    id_asignatura = AsignaturaSerializer()
    class Meta:
        model = Coordinacion_Seccion      
        fields = ('coordinacion','seccion', 'bloques_horario', 'id_asignatura')  
        
class EvaluacionSerializer(serializers.ModelSerializer):
    id_coordinacion = CoordinacionSeccionSerializer()
    class Meta:
        model = Evaluacion   
        fields = ('id','nombre','ponderacion','estado','id_coordinacion')  

class EstudianteSerializer(serializers.ModelSerializer):
    id_usuario = UsuariosSerializers()
    class Meta:
        model = Estudiante   
        fields = ('id','rut','dig_verificador','id_usuario')  


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente  
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    id_evaluacion = EvaluacionSerializer()
    id_estudiante = EstudianteSerializer()

    class Meta:
        model = Calificacion      
        fields = ('nota','fecha_entrega','id_evaluacion','id_estudiante','id_observacion')  

class SolicitudSerializer(serializers.ModelSerializer):
    id_evaluacion = EvaluacionSerializer()
    class Meta:
        model = Solicitud_Revision
        fields = '__all__'

class CoordinacionEstudianteSerializer(serializers.ModelSerializer):
    #id_estudiante = EstudianteSerializer()
    id_coordinacion = CoordinacionSeccionSerializer()
    class Meta:
        model = Coordinacion_Estudiante    
        fields = ('promedioEstudiante','id_estudiante','id_coordinacion')

class CoordinacionDocenteSerializer(serializers.ModelSerializer):
    #id_docente = DocenteSerializer()
    id_coordinacion = CoordinacionSeccionSerializer()
    class Meta:
        model = Coordinacion_Docente    
        fields = ('id_docente','id_coordinacion')
#Serializer para mostrar datos en respuesta de solicitud
class SolicitudRespuestaSerializer(serializers.ModelSerializer):
    id_estudiante = EstudianteSerializer()
    id_evaluacion = EvaluacionSerializer()
    class Meta:
        model = Solicitud_Revision
        fields = ('motivo', 'id_evaluacion','id_estudiante')

#Serializer para actualizar datos en respuesta de solicitud
class SolicitudActualizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud_Revision
        fields = '__all__'

# Encontrar la calificacion sin ningun dato adicional
class CalificacionEspecificaSerializer(serializers.ModelSerializer):
    #id_evaluacion = EvaluacionSerializer()
    class Meta:
        model = Calificacion      
        fields = '__all__'




        
