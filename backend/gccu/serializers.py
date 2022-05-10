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

class TipoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Evaluacion
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

# Serializer modificado por Miguel. Para utilizarlo en las evaluaciones que tiene un curso.       
class EvaluacionSerializer(serializers.ModelSerializer):
    id_coordinacion = CoordinacionSeccionSerializer()
    id_tipoEvaluacion = TipoEvaluacionSerializer()
    
    class Meta:
        model = Evaluacion   
        fields = ('id','nombre','ponderacion','estado', 'fechaEvActual', 'id_coordinacion', 'id_tipoEvaluacion')

# Serializer exclusivo para agregar evaluaciones.
class PostEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

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


######################################################################################33
## Saber las secciones de un coordinador con su asignatura
class CoordinacionCoordinadorSerializer(serializers.ModelSerializer):
    id_asignatura = AsignaturaSerializer()
    class Meta:
        model = Coordinacion_Seccion      
        fields = '__all__'  


# Para obtener las solicitudes respecto a un curso - 2
class SolicitudesEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion  
        fields = ('id_coordinacion','id_docente')  
# Para obtener las solicitudes respecto a un curso - 1
class SolicitudesDocenteCursoSerializer(serializers.ModelSerializer):
    id_evaluacion = SolicitudesEvaluacionSerializer()
    class Meta:
        model = Solicitud_Revision     
        fields = ('id_docente','id_evaluacion')  
###########################################################################################

# Obtener los planes de estudios pertenecientes a un jefe de carrera - 1
class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera  
        fields = ('id','id_jefeCarrera')  

# Obtener los planes de estudios pertenecientes a un jefe de carrera - 2
class PlanEstudioSerializer(serializers.ModelSerializer):
    id_carrera = CarreraSerializer()
    class Meta:
        model = Plan_Estudio
        fields = ('id','id_carrera')  

# Obtener los planes de estudios pertenecientes a un jefe de carrera - 1
class PlanesJefeSerializer(serializers.ModelSerializer):
    id_planEstudio = PlanEstudioSerializer()
    class Meta:
        model = Asignaturas_PlanEstudio  
        fields = '__all__'  

class CoordinacionSeccionV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinacion_Seccion      
        fields = ('id','coordinacion','seccion', 'bloques_horario', 'id_asignatura')  



        
