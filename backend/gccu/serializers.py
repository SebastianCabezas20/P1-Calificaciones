from rest_framework import serializers
from .models import *

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura      
        fields = '__all__'  


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion   
        fields = ('nombre','ponderacion','estado')  

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante   
        fields = ('rut','dig_verificador')  

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
        fields = ('coordinacion','seccion','id_asignatura')  


