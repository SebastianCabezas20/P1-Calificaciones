from dataclasses import field
from pyexpat import model
from psycopg2 import Date
from rest_framework import serializers
from .models import *
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RolesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    id_usuario = UsuariosSerializers()
    class Meta:
        model = Docente  
        fields = ('id', 'rut', 'dig_verificador', 'id_usuario')

class CoordinadorSerializers(serializers.ModelSerializer):
    id_usuario = UsuariosSerializers()
    class Meta:
        model = Coordinador
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
        fields = ('id', 'coordinacion','seccion', 'bloques_horario', 'id_asignatura') 

class CoordinacionDocenteSerializer(serializers.ModelSerializer):
    #id_docente = DocenteSerializer()
    id_coordinacion = CoordinacionSeccionSerializer()
    class Meta:
        model = Coordinacion_Docente    
        fields = ('id', 'id_coordinacion')

# Serializer modificado por Miguel. Para utilizarlo en las evaluaciones que tiene un curso.       
class EvaluacionSerializer(serializers.ModelSerializer):
    id_coordinacion = CoordinacionSeccionSerializer()
    id_tipoEvaluacion = TipoEvaluacionSerializer()
    id_docente = DocenteSerializer()
    
    class Meta:
        model = Evaluacion
        fields = ('id', 'nombre', 'fechaEvActual', 'fechaEntrega', 'ponderacion', 'estado', 'id_tipoEvaluacion', 'id_docente', 'id_observacion', 'id_coordinacion')

# Serializer exclusivo para agregar evaluaciones.
class PostEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'
#Serializer que ayuda a obtener el id del estudiante, dado su id de usuario.
class EstudianteSerializer(serializers.ModelSerializer):
    id_usuario = UsuariosSerializers()
    class Meta: 
        model = Estudiante   
        fields = ('id','rut','dig_verificador','id_usuario')  

# Serializer que ayuda a obtener el id del jefe de carrera, dado su id de usuario.
class JefeCarreraSerializer(serializers.ModelSerializer):
    id_usuario = UsuariosSerializers()
    class Meta:
        model = Jefe_Carrera  
        fields = ('id', 'rut', 'dig_verificador', 'id_usuario')
    
# Serializer que ayuda a obtener el id del coordinador, dado su id de usuario.
class CoordinadorSerializer(serializers.ModelSerializer):
    id_usuario = UsuariosSerializers()
    class Meta:
        model = Coordinador 
        fields = ('id', 'rut', 'dig_verificador', 'id_usuario')

class CalificacionSerializer(serializers.ModelSerializer):
    id_evaluacion = EvaluacionSerializer()
    id_estudiante = EstudianteSerializer()
    fecha_entrega = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Calificacion      
        fields = '__all__'  

## Usado para ver la solicitudes de una asignatura
class SolicitudSerializer(serializers.ModelSerializer):
    id_evaluacion = EvaluacionSerializer()
    id_estudiante = EstudianteSerializer()
    id_docente = DocenteSerializer()
    class Meta:
        model = Solicitud_Revision
        fields = '__all__'

# Modificado: Se quito el comentario de id_estudiante.
class CoordinacionEstudianteSerializer(serializers.ModelSerializer):
    id_estudiante = EstudianteSerializer()
    id_coordinacion = CoordinacionSeccionSerializer()
    class Meta:
        model = Coordinacion_Estudiante    
        fields = ('promedioEstudiante','id_estudiante','id_coordinacion')



#Serializer para mostrar datos en respuesta de solicitud
class SolicitudRespuestaSerializer(serializers.ModelSerializer):
    id_estudiante = EstudianteSerializer()
    id_evaluacion = EvaluacionSerializer()
    class Meta:
        model = Solicitud_Revision
        fields = '__all__'

#Serializer para actualizar datos en respuesta de solicitud
class SolicitudActualizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud_Revision
        fields = '__all__'

# Encontrar la calificacion sin ningun dato adicional
class CalificacionEspecificaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calificacion      
        fields = '__all__'


######################################################################################33
## Saber las secciones de un coordinador con su asignatura - 2
class CoordinacionCoordinadorSerializer(serializers.ModelSerializer):
    id_asignatura = AsignaturaSerializer()
    class Meta:
        model = Coordinacion_Seccion      
        fields = '__all__'  
## Saber las secciones de un coordinador con su asignatura - 1
class DocenteCursoSerializer(serializers.ModelSerializer):
    id_coordinacion = CoordinacionCoordinadorSerializer()
    id_docente = DocenteSerializer()
    class Meta:
        model = Coordinacion_Docente      
        fields = '__all__'  


# Para obtener las solicitudes respecto a un curso - 2
class SolicitudesEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion  
        fields = ('id','id_coordinacion','nombre')  
# Para obtener las solicitudes respecto a un curso - 1
class SolicitudesDocenteCursoSerializer(serializers.ModelSerializer):
    id_evaluacion = SolicitudesEvaluacionSerializer()
    id_estudiante = EstudianteSerializer()
    class Meta:
        model = Solicitud_Revision     
        fields ='__all__'  
###########################################################################################

# Obtener los planes de estudios pertenecientes a un jefe de carrera - 3
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
        
# Obtener los planes de estudios pertenecientes a un jefe de carrera - 2
class AsignaturaV2Serializer(serializers.ModelSerializer):
    id_coordinador = CoordinadorSerializers()
    class Meta:
        model = Asignatura      
        fields = '__all__'  

# Obtener los planes de estudios pertenecientes a un jefe de carrera - 1
class PlanesJefeSerializer(serializers.ModelSerializer):
    id_planEstudio = PlanEstudioSerializer()
    id_asignatura = AsignaturaV2Serializer()
    class Meta:
        model = Asignaturas_PlanEstudio  
        fields = '__all__'  

class CoordinacionSeccionV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinacion_Seccion      
        fields = ('id','coordinacion','seccion', 'bloques_horario', 'id_asignatura')  


class EvaluacionEspecificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion      
        fields = '__all__'

class CalificacionSerializerNoDate(serializers.ModelSerializer):
    id_evaluacion = EvaluacionSerializer()
    id_estudiante = EstudianteSerializer()
    class Meta:
        model = Calificacion      
        fields = '__all__' 

class CalificacionEspecificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion      
        fields = '__all__'