from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.core import serializers
import json

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
     
    serializer = CalificacionSerializer(calificaciones, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getDataSolicitud(request):
    print(Solicitud_Revision.objects.select_related('id_estudiante').filter(id_estudiante__id = 2).all().query)
    solicitudes = Solicitud_Revision.objects.select_related('id_estudiante').filter(id_estudiante__id = "2").all()

    serializer = SolicitudSerializer(solicitudes, many = "true")
    return Response(serializer.data)

@api_view(['GET'])
def getCursosByEstudiante(request):
    
    print(Coordinacion_Estudiante.objects.filter(id_estudiante__id = 3).query)
    ces = Coordinacion_Estudiante.objects.filter(id_estudiante__id = 3)

    serializer = CoordinacionEstudianteSerializer(ces, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCursosByDocente(request):
    
    print(Coordinacion_Docente.objects.filter(id_docente__id = 1).query)
    cds = Coordinacion_Docente.objects.filter(id_docente__id = 1)

    serializer = CoordinacionDocenteSerializer(cds, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getEstudiante(request):
    
    print(Estudiante.objects.filter(id = 3).query)
    estudiantes = Estudiante.objects.filter(id=3)

    serializer = EstudianteSerializer(estudiantes, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def prueba(request):
    
    print(Coordinacion_Estudiante.objects.filter(id_estudiante__id = 3).query)
    ces = Coordinacion_Estudiante.objects.filter(id_estudiante__id = 3)

    serializer = CoordinacionEstudianteSerializer(ces, many="true")

@api_view(['GET'])
def getDataSolicitudesDocente(request):

    print(Solicitud_Revision.objects.filter(id_docente__rut = 20900900).query)
    solicitudes = Solicitud_Revision.objects.filter(id_docente__rut = 20900900)

    serializer = SolicitudSerializer(solicitudes, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCalificacionesPerCursoDocente(request):

    print(Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = "10110", id_evaluacion__id_coordinacion__id_asignatura__componente = "T").all().query)
    
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = "10110", id_evaluacion__id_coordinacion__id_asignatura__componente = "T").all()

    serializer = CalificacionSerializer(calificaciones, many='true')
    return Response(serializer.data)

## Obtener informacion para realizar la respuesta a una apelacion
@api_view(['GET'])
def getDataSolicitudRespuesta(request):
    print(Solicitud_Revision.objects.filter(id_estudiante__id = 2).all().query)
    solicitudes = Solicitud_Revision.objects.filter(id_estudiante__id = 2, id_evaluacion__id = 2).all()
    #Cambiar ids respecto a la solicitud realizada deberian ser las mismas
    nota = Calificacion.objects.filter(id_estudiante = 2, id_evaluacion = 1).all()
    #idEvaluacion = Solicitud_Revision.objects.filter(id_estudiante__id = 2).values('id_evaluacion').first().get('id_evaluacion')
    #print(idEvaluacion)
    serializer = SolicitudRespuestaSerializer(solicitudes, many = "true")
    serializerNota = CalificacionEspecificaSerializer(nota, many = "true")
    return Response([serializer.data,serializerNota.data])

#####################POSIBLE COMBINACION DE SERIALIZERS getDataSolicitudRespuesta
## Actualizacion de Solicitud respuesta id_motivo y id_calificacion para cambiar nota
@api_view(['GET','PUT'])
def actualizacionSolicitudRespuesta(request):

    if request.method == 'GET':
        solicitud = Solicitud_Revision.objects.all()
        solicituds = SolicitudActualizacionSerializer(solicitud, many = "true")
        return Response(solicituds.data)
    elif request.method == 'PUT':
        print("---------------------------------------------------------")
        solicitud = Solicitud_Revision.objects.filter(id = 2).first()
        solicitud_actualizada = SolicitudActualizacionSerializer(solicitud, data = request.data)
        if solicitud_actualizada.is_valid():
            solicitud_actualizada.save()
            return Response(solicitud_actualizada.data)
        return Response(solicitud_actualizada.errors)


@api_view(['GET','PUT'])
def actualizacionCalificacionEstudiante(request):

    if request.method == 'GET':
        calificacion = Calificacion.objects.all()
        calificacions = CalificacionEspecificaSerializer(calificacion, many = "true")
        return Response(calificacions.data)
    elif request.method == 'PUT':
        print("---------------------------------------------------------")
        calificacion = Calificacion.objects.filter(id = 5).first()
        calificacion_actualizada = CalificacionEspecificaSerializer(calificacion, data = request.data)
        if calificacion_actualizada.is_valid():
            calificacion_actualizada.save()
            return Response(calificacion_actualizada.data)
        return Response(calificacion_actualizada.errors)
    

    return Response(serializer.data)

# Primera parte para la subida de planilla de calificaciones.
@api_view(['GET'])
def getCalifiacionesEstudiantes(request):
    
    calificacionEstudiantes = Calificacion.objects.filter(id_evaluacion__id = 4).all()
    
    serializer = CalificacionSerializer(calificacionEstudiantes, many="true")
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def evaluacionesCoordinacion(request, idEvaluacion = None):

    # Falta comprobar que el docente hace clase en cierta coordinacion (eso cuando ya se tenga el id de la vista).
    if request.method == 'GET':
        evaluacionCoordinacion = Evaluacion.objects.filter(id_coordinacion__id = 2).all()
        serializer = EvaluacionSerializer(evaluacionCoordinacion, many = "true")
        return Response(serializer.data)
    
    # Funcionando correctamente.
    if request.method == 'DELETE':
        evaluacion = Evaluacion.objects.filter(id = idEvaluacion).first()
        evaluacion.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getTiposEvaluaciones(request):
    tiposEvaluaciones = Tipo_Evaluacion.objects.all()
    serializer = TipoEvaluacionSerializer(tiposEvaluaciones, many="true")
    return Response(serializer.data)