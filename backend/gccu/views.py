from distutils.log import error
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.contrib.auth.models import User, Group

@api_view(['GET'])
def getDocente(request, idUsuario = None):
    infoDocente = Docente.objects.filter(id_usuario__id = idUsuario).first()
    serializer = DocenteSerializer(infoDocente)
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

# Solicitudes de revisión realizadas por un estudiante.
@api_view(['GET'])
def getDataSolicitud(request, idUsuario = None):
    solicitudes = Solicitud_Revision.objects.filter(id_estudiante__id_usuario__id = idUsuario).all()
    serializer = SolicitudSerializer(solicitudes, many = "true")
    return Response(serializer.data)

@api_view(['GET'])
def getCursosByEstudiante(request):
    
    print(Coordinacion_Estudiante.objects.filter(id_estudiante__id = 3).query)
    ces = Coordinacion_Estudiante.objects.filter(id_estudiante__id = 3)

    serializer = CoordinacionEstudianteSerializer(ces, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCursosByDocente(request, idUsuario = None):
    cursosDocente = Coordinacion_Docente.objects.filter(id_docente__id_usuario__id = idUsuario).all()
    serializer = CoordinacionDocenteSerializer(cursosDocente, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getEstudiante(request):
    
    print(Estudiante.objects.filter(id = 3).query)
    estudiantes = Estudiante.objects.filter(id=3)

    serializer = EstudianteSerializer(estudiantes, many="true")
    return Response(serializer.data)

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

@api_view(['GET'])
def getAsignaturastoCoordinador(request):

    print(Asignatura.objects.filter(id_coordinador = 1).query)
    coordinador = Asignatura.objects.filter(id_coordinador = 1)

    serializer = AsignaturaSerializer(coordinador, many = 'true')
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

## ACtualizacion de calificaciones de una solicitud
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
    

# Primera parte para la subida de planilla de calificaciones.
@api_view(['GET'])
def getCalifiacionesEstudiantes(request):
    
    calificacionEstudiantes = Calificacion.objects.filter(id_evaluacion__id = 4).all()
    
    serializer = CalificacionSerializer(calificacionEstudiantes, many="true")
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'POST'])
def evaluacionesCoordinacion(request, idEvaluacion = None, idCoordinacion = None):

    # Funcionando.
    if request.method == 'GET':
        evaluacionCoordinacion = Evaluacion.objects.filter(id_coordinacion__id = idCoordinacion).all()
        serializer = EvaluacionSerializer(evaluacionCoordinacion, many = "true")
        return Response(serializer.data)
    
    # Funcionando correctamente.
    if request.method == 'DELETE':
        evaluacion = Evaluacion.objects.filter(id = idEvaluacion).first()
        evaluacion.delete()
        return Response(status=status.HTTP_200_OK)

    # Funcionando correctamente. Salvo problemas en la vista.
    if request.method == 'POST':
        evaluacionAgregada = PostEvaluacionSerializer(data = request.data)
        if evaluacionAgregada.is_valid():
            evaluacionAgregada.save()
            return Response(evaluacionAgregada.data)
        return Response(evaluacionAgregada.errors)

@api_view(['GET'])
def getTiposEvaluaciones(request):
    tiposEvaluaciones = Tipo_Evaluacion.objects.all()
    serializer = TipoEvaluacionSerializer(tiposEvaluaciones, many="true")
    return Response(serializer.data)

# Saber que coordinacion quiere visualizar, de aqui sacar el id para ver la tabla Solicitud -> CursoInscrito
@api_view(['GET'])
def getCoordinacionesCoordinador(request, idCoordinador = None):
    ### ID del coordinador
    coordinacionesCoordinador = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__id_coordinador = idCoordinador).all()
    
    serializer = DocenteCursoSerializer(coordinacionesCoordinador, many="true")
    return Response(serializer.data)

## LUego de especificar la seccion se recogen las solicitudes de este curso-seccion id para ver la tabla Solicitud -> CursoInscrito
@api_view(['GET'])
def getSolicitudesCurso(request, idCoordinacion = None):
    
    ### ID de cursoInscrito o Coordinacion Seccion
    solicitudesCurso = Solicitud_Revision.objects.filter(id_evaluacion__id_coordinacion = idCoordinacion).all()
    
    serializer = SolicitudesDocenteCursoSerializer(solicitudesCurso, many="true")
    return Response(serializer.data)

## Asignaturas de un jefe de carrera
@api_view(['GET'])
def getAsignaturasJefeCarrera(request, idJefe = None):
    ### ID jefe de carrera, se mostraran sus asignaturas
    planesEstudio = Asignaturas_PlanEstudio.objects.filter(id_planEstudio__id_carrera__id_jefeCarrera = idJefe).distinct('id_asignatura').all()
    
    serializer = PlanesJefeSerializer(planesEstudio, many="true")
    return Response(serializer.data)

## Solicitudes de una asignatura (Jefe de carrera)
@api_view(['GET'])
def getSolicitudesAsignaturaJefeCarrera(request, idAsignatura = None):
    ## ID asignatura seleccionado jefe de carrera
    solicitudes = Solicitud_Revision.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__id = idAsignatura).all()
    
    serializer = SolicitudSerializer(solicitudes, many="true")
    return Response(serializer.data)

## Modificar fecha de una evaluación
@api_view(['PUT'])
def updateFechaEvaluacion(request, idEvaluacion = None):
    evaluacion = Evaluacion.objects.get(id = idEvaluacion)
    evaluacion_actualizada = EvaluacionEspecificaSerializer(evaluacion, data = request.data)
    if evaluacion_actualizada.is_valid():
        evaluacion_actualizada.save()
        print(evaluacion_actualizada.data)
        return Response(evaluacion_actualizada.data)
    print(evaluacion_actualizada.errors)
    return Response(evaluacion_actualizada.errors)
    
@api_view(['GET'])
def getAllEvaluaciones(request):
    evaluacionCoordinacion = Evaluacion.objects.filter(id_coordinacion__id = 1).all()
    serializer = EvaluacionEspecificaSerializer(evaluacionCoordinacion, many = "true")
    return Response(serializer.data)

@api_view(['GET'])
def getRolesUsuarios(request):
    roles = Group.objects.all()
    serializer = RolesSerializers(roles, many = "true")
    return Response(serializer.data)

@api_view(['POST'])
def isRolUser(request):

    if User.objects.filter(username = request.data.get('nombreUsuario'), groups = request.data.get('idRolSeleccionado')).exists():
        usuarioExiste = User.objects.filter(username = request.data.get('nombreUsuario')).first()
        serializer = UsuariosSerializers(usuarioExiste)
        return Response(serializer.data)
    return Response(error)