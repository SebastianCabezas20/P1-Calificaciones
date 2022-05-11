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

# Vista que retorna el docente, dado su id de usuario.
@api_view(['GET'])
def getJefeCarrera(request, idUsuario = None):
    infoJefe = Jefe_Carrera.objects.filter(id_usuario__id = idUsuario).first()
    serializer = JefeCarreraSerializer(infoJefe)
    return Response(serializer.data)

# Vista que retorna el coordinador, dado su id de usuario.
@api_view(['GET'])
def getCoordinador(request, idUsuario = None):
    infoCoordinador = Coordinador.objects.filter(id_usuario__id = idUsuario).first()
    serializer = CoordinadorSerializer(infoCoordinador)
    return Response(serializer.data)

# Vista que retorna el estudiante, dado su id de usuario.
@api_view(['GET'])
def getIdEstudiante(request, idUsuario = None):
    infoCoordinador = Estudiante.objects.filter(id_usuario__id = idUsuario).first()
    serializer = EstudianteSerializer(infoCoordinador)
    return Response(serializer.data)

@api_view(['GET'])
def getDataAsignatura(request, codigo = None):
    
    #Prueba codigo 10110 id estudiante 1    
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = codigo, id_evaluacion__id_coordinacion__id_asignatura__componente = "T", id_estudiante__id = "1").all()
    serializer = CalificacionSerializer(calificaciones, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getDataAsignaturaLab(request, codigo = None):
    
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = codigo, id_evaluacion__id_coordinacion__id_asignatura__componente = "L", id_estudiante__id = "1").all()
    serializer = CalificacionSerializer(calificaciones, many="true")
    return Response(serializer.data)

##Obtener la informacion del curso - asignatura lab
@api_view(['GET'])
def getInformacionCursoLab(request, codigo = None):
    
    informacion = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__codigo = codigo, id_coordinacion__id_asignatura__componente = "L").all()
    serializer = DocenteCursoSerializer(informacion, many="true")
    return Response(serializer.data)

##Obtener la informacion del curso - asignatura Teoria
@api_view(['GET'])
def getInformacionCursoTeoria(request, codigo = None):
    
    ## codigo 10110 
    informacion = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__codigo = codigo, id_coordinacion__id_asignatura__componente = "T" ).all()
    serializer = DocenteCursoSerializer(informacion, many="true")
    return Response(serializer.data)

## Informacion para la apelacion de un estudiante
@api_view(['GET'])
def getDataSolicitudApelacion(request, idCalificacion = None):
    
    calificaciones = Calificacion.objects.filter(id = idCalificacion).all()
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
    ces = Coordinacion_Estudiante.objects.filter(id_estudiante__id = 1)

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

    print(Solicitud_Revision.objects.all())
    solicitudes = Solicitud_Revision.objects.all()

    serializer = SolicitudSerializer(solicitudes, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCalificacionesPerAsignaturaEvaluacion(request, idAsignatura, idEvaluacion):

    print(Calificacion.objects.filter(id_evaluacion__id_coordinacion = idAsignatura, id_evaluacion = idEvaluacion ).all().query)
    
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion = idAsignatura, id_evaluacion = idEvaluacion ).all()

    serializer = CalificacionSerializer(calificaciones, many='true')
    return Response(serializer.data)

@api_view(['GET'])
def getAsignaturastoCoordinador(request, idCoordinador = None):

    # 1
    print(Asignatura.objects.filter(id_coordinador = idCoordinador).query)
    coordinador = Asignatura.objects.filter(id_coordinador = 1)

    serializer = AsignaturaSerializer(coordinador, many = 'true')
    return Response(serializer.data)

## Obtener informacion para realizar la respuesta a una apelacion
## ID estudiante - ID evaluacion - 
@api_view(['GET'])
def getDataSolicitudRespuesta(request,idEstudiante = None, idEvaluacion = None):
    ## Prueba idEstudiante 2 IdEval 2
    print(Solicitud_Revision.objects.filter(id_estudiante__id = 2).all().query)
    solicitudes = Solicitud_Revision.objects.filter(id_estudiante__id = idEstudiante, id_evaluacion__id = idEvaluacion).all()
    #Cambiar ids respecto a la solicitud realizada deberian ser las mismas
    nota = Calificacion.objects.filter(id_estudiante = idEstudiante, id_evaluacion = idEvaluacion).all()
    #idEvaluacion = Solicitud_Revision.objects.filter(id_estudiante__id = 2).values('id_evaluacion').first().get('id_evaluacion')
    #print(idEvaluacion)
    serializer = SolicitudRespuestaSerializer(solicitudes, many = "true")
    serializerNota = CalificacionEspecificaSerializer(nota, many = "true")
    return Response([serializer.data,serializerNota.data])

#####################POSIBLE COMBINACION DE SERIALIZERS getDataSolicitudRespuesta
## Actualizacion de Solicitud respuesta id_motivo y id_calificacion para cambiar nota
@api_view(['GET','PUT'])
def actualizacionSolicitudRespuesta(request, idSolicitud = None):

    if request.method == 'GET':
        solicitud = Solicitud_Revision.objects.all()
        solicituds = SolicitudActualizacionSerializer(solicitud, many = "true")
        return Response(solicituds.data)
    elif request.method == 'PUT':
        print("---------------------------------------------------------")
        #### ID de la solicitud  ## Prueba 2
        solicitud = Solicitud_Revision.objects.filter(id = idSolicitud).first()
        solicitud_actualizada = SolicitudActualizacionSerializer(solicitud, data = request.data)
        if solicitud_actualizada.is_valid():
            solicitud_actualizada.save()
            return Response(solicitud_actualizada.data)
        return Response(solicitud_actualizada.errors)

## ACtualizacion de calificaciones de una solicitud
@api_view(['GET','PUT'])
def actualizacionCalificacionEstudiante(request, idCalificacion = None):

    if request.method == 'GET':
        calificacion = Calificacion.objects.all()
        calificacions = CalificacionEspecificaSerializer(calificacion, many = "true")
        return Response(calificacions.data)
    elif request.method == 'PUT':
        print("---------------------------------------------------------")
        ### ID de calificacion a modificar Prueba 2
        calificacion = Calificacion.objects.filter(id = idCalificacion).first()
        calificacion_actualizada = CalificacionEspecificaSerializer(calificacion, data = request.data)
        if calificacion_actualizada.is_valid():
            calificacion_actualizada.save()
            return Response(calificacion_actualizada.data)
        return Response(calificacion_actualizada.errors)
    
# Obtiene los estudiantes que estan inscitos en una coordinacion. 
# Se cargan en la vista de subir calificaciones.
@api_view(['GET'])
def getCalifiacionesEstudiantes(request, idCoordinacion = None):
    calificacionEstudiantes = Coordinacion_Estudiante.objects.filter(id_coordinacion__id = idCoordinacion).all()
    serializer = CoordinacionEstudianteSerializer(calificacionEstudiantes, many="true")
    return Response(serializer.data)    

@api_view(['GET', 'DELETE', 'POST', 'PUT'])
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

    # Funcionando correctamente.
    if request.method == 'POST':
        evaluacionAgregada = PostEvaluacionSerializer(data = request.data)
        if evaluacionAgregada.is_valid():
            evaluacionAgregada.save()
            return Response(evaluacionAgregada.data)
        return Response(evaluacionAgregada.errors)
    
    # Funcionando correctamente. Modificar una evaluacion.
    if request.method == 'PUT':
        evaluacion = Evaluacion.objects.get(id = idEvaluacion)
        evaluacion_actualizada = EvaluacionEspecificaSerializer(evaluacion, data = request.data)
        if evaluacion_actualizada.is_valid():
            evaluacion_actualizada.save()
            print(evaluacion_actualizada.data)
            return Response(evaluacion_actualizada.data)
        return Response(evaluacion_actualizada.errors)

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
    
@api_view(['GET'])
def getAllEvaluaciones(request, idCoordinacion = None):
    evaluacionCoordinacion = Evaluacion.objects.filter(id_coordinacion__id = idCoordinacion).all()
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

@api_view(['POST'])
def calificacionesEstudiantes(request):
    calificacion = CalificacionEspecificaSerializer(data = request.data)
    if calificacion.is_valid():
        calificacion.save()
        return Response(calificacion.data)
    return Response(calificacion.errors)

# Obtener los datos de una evaluación en particular. Cambiar el estado de una evaluacion.
@api_view(['GET', 'PUT'])
def crudOneEvaluacion(request, idEvaluacion = None):
    
    if request.method == 'GET':
        test = Evaluacion.objects.filter(id = idEvaluacion).first()
        serializer = PostEvaluacionSerializer(test)
        return Response(serializer.data)

@api_view(['GET'])
def getSolicitudesByIdDocente(request, idDocente):

    print(Solicitud_Revision.objects.filter(id_docente__id = idDocente).query)
    solicitudes = Solicitud_Revision.objects.filter(id_docente__id = idDocente)

    serializer = SolicitudSerializer(solicitudes, many="true")
    return Response(serializer.data)