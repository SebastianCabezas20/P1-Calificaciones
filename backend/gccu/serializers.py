from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura      
        fields = '__all__'  

class CoordinacionSeccionSerializer(serializers.ModelSerializer):
    id_asignatura = AsignaturaSerializer()
    class Meta:
        model = Coordinacion_Seccion      
        fields = ('coordinacion','seccion','id_asignatura') 
        
class EvaluacionSerializer(serializers.ModelSerializer):
    id_coordinacion = CoordinacionSeccionSerializer()
    class Meta:
        model = Evaluacion   
        fields = ('nombre','ponderacion','estado','id_coordinacion')  

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante   
        fields = ('id','rut','dig_verificador')  

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

class CoordinacionSeccionSerializer(serializers.ModelSerializer):
    id_asignatura = AsignaturaSerializer()
    class Meta:
        model = Coordinacion_Seccion      
        fields = ('coordinacion','seccion', 'bloques_horario', 'id_asignatura')  

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