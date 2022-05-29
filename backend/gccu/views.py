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
def getDataAsignatura(request, codigo = None, idUsuario = None):  
    ## Evaluaciones con calificaciones
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = codigo, id_evaluacion__id_coordinacion__id_asignatura__componente = "T", id_estudiante__id_usuario__id = idUsuario).all()
    ##Evaluaciones sin evaluar
    evaluacionesSinNota = Evaluacion.objects.filter(estado = 'P',id_coordinacion__id_asignatura__codigo = codigo,id_coordinacion__id_asignatura__componente = "T")
    serializerEvaluaciones = EvaluacionEspecificaSerializer(evaluacionesSinNota, many = 'true')
    serializer = CalificacionSerializer(calificaciones, many="true")
    ## Respuesta 
    return Response([serializer.data,serializerEvaluaciones.data])

@api_view(['GET'])
def getDataAsignaturaLab(request, codigo = None, idUsuario = None):
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__codigo = codigo, id_evaluacion__id_coordinacion__id_asignatura__componente = "L", id_estudiante__id_usuario__id = idUsuario).all()
    serializer = CalificacionSerializer(calificaciones, many="true")
    ## Evaluaciones sin nota
    evaluacionesSinNota = Evaluacion.objects.filter(estado = 'P',id_coordinacion__id_asignatura__codigo = codigo,id_coordinacion__id_asignatura__componente = "L")
    serializerEvaluaciones = EvaluacionEspecificaSerializer(evaluacionesSinNota, many = 'true')
    return Response([serializer.data,serializerEvaluaciones.data])

# Obtener la informacion del curso - asignatura lab
@api_view(['GET'])
def getInformacionCursoLab(request, codigo = None):  
    informacion = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__codigo = codigo, id_coordinacion__id_asignatura__componente = "L").all()
    serializer = DocenteCursoSerializer(informacion, many="true")
    return Response(serializer.data)

# Obtener la informacion del curso - asignatura Teoria
@api_view(['GET'])
def getInformacionCursoTeoria(request, codigo = None):
    informacion = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__codigo = codigo, id_coordinacion__id_asignatura__componente = "T").all()
    serializer = DocenteCursoSerializer(informacion, many="true")
    return Response(serializer.data)

# Informacion para la apelacion de un estudiante
@api_view(['GET'])
def getDataSolicitudApelacion(request, idCalificacion = None):
    calificaciones = Calificacion.objects.filter(id = idCalificacion).all()
    serializer = CalificacionSerializer(calificaciones, many = "true")
    return Response(serializer.data)

# Solicitudes de revisión realizadas por un estudiante.
@api_view(['GET', 'PUT' ,'POST'])
def dataSolicitud(request, idUsuario = None, idSolicitud = None):
    if request.method == 'GET':
        solicitudes = Solicitud_Revision.objects.filter(id_estudiante__id_usuario__id = idUsuario).all()
        serializer = SolicitudSerializer(solicitudes, many = "true")
        return Response(serializer.data)
    
    if request.method == 'PUT':
        solicitud = Solicitud_Revision.objects.filter(id = idSolicitud).first()
        solicitud_actualizada = OnlySolicitudSerializer(solicitud, data = request.data)
        if solicitud_actualizada.is_valid():
            solicitud_actualizada.save()
            return Response(solicitud_actualizada.data)
        return Response(solicitud_actualizada.errors)

    if request.method == 'POST':
        nuevaSolicitud = OnlySolicitudSerializer(data = request.data)
        if nuevaSolicitud.is_valid():
            nuevaSolicitud.save()
            return Response(nuevaSolicitud.data)
        return Response(nuevaSolicitud.errors)

@api_view(['GET'])
def getCursosByEstudiante(request, idUsuario = None):
    cursos = Coordinacion_Estudiante.objects.filter(id_estudiante__id_usuario__id = idUsuario).distinct('id_coordinacion__id_asignatura__codigo')
    serializer = CoordinacionEstudianteSerializer(cursos, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCursosByDocente(request, idUsuario = None):
    cursosDocente = Coordinacion_Docente.objects.filter(id_docente__id_usuario__id = idUsuario).all()
    serializer = CoordinacionDocenteSerializer(cursosDocente, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getEstudiante(request):
    estudiantes = Estudiante.objects.filter(id=3)
    serializer = EstudianteSerializer(estudiantes, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCalificacionesPerAsignaturaEvaluacion(request, idAsignatura, idEvaluacion):
    calificaciones = Calificacion.objects.filter(id_evaluacion__id_coordinacion = idAsignatura, id_evaluacion = idEvaluacion ).all()
    serializer = CalificacionSerializer(calificaciones, many='true')
    return Response(serializer.data)

@api_view(['GET'])
def getAsignaturastoCoordinador(request, idCoordinador = None):
    coordinador = Asignatura.objects.filter(id_coordinador = 1)
    serializer = AsignaturaSerializer(coordinador, many = 'true')
    return Response(serializer.data)

## Obtener informacion para realizar la respuesta a una apelacion
## ID estudiante - ID evaluacion - 
@api_view(['GET'])
def getDataSolicitudRespuesta(request,idEstudiante = None, idEvaluacion = None):
    ## Solicitud segun ID estudiante y ID evaluacion
    solicitudes = Solicitud_Revision.objects.filter(id_estudiante__id = idEstudiante, id_evaluacion__id = idEvaluacion).all()
    serializer = SolicitudRespuestaSerializer(solicitudes, many = "true")
    return Response(serializer.data)

## ACtualizacion de calificaciones de una solicitud
@api_view(['GET','PUT'])
def actualizacionCalificacionEstudiante(request, idCalificacion = None):

    if request.method == 'GET':
        calificacion = Calificacion.objects.all()
        calificacions = CalificacionEspecificaSerializer(calificacion, many = "true")
        return Response(calificacions.data)
    
    if request.method == 'PUT':
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
            return Response(evaluacion_actualizada.data)
        return Response(evaluacion_actualizada.errors)

@api_view(['GET'])
def getTiposEvaluaciones(request):
    tiposEvaluaciones = Tipo_Evaluacion.objects.all()
    serializer = TipoEvaluacionSerializer(tiposEvaluaciones, many="true")
    return Response(serializer.data)

# Arreglar esta vista para que entregue las coordinaciones con los profesores agrupados (2 o más profesores). ## Solucionado
# Saber que coordinacion quiere visualizar, de aqui sacar el id para ver la tabla Solicitud -> CursoInscrito
@api_view(['GET'])
def getCoordinacionesCoordinador(request, idCoordinador = None):
    coordinacionesCoordinador = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__id_coordinador = idCoordinador)
    idsCoordinacion = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__id_coordinador = idCoordinador).distinct('id_coordinacion__id').values_list('id_coordinacion__id', flat=True)
    #print(idsCoordinacion)
    arregloInformacion = []
    for id in idsCoordinacion:
        coordinacion_docentes = Coordinacion_Docente.objects.filter(id_coordinacion__id = id)
        arregloInformacion.append(DocenteCursoSerializer(coordinacion_docentes, many="true").data)
    #serializer = DocenteCursoSerializer(coordinacionesCoordinador, many="true")
    return Response(arregloInformacion)

@api_view(['GET'])
def getCoordinacionesAsignatura(request, idAsignatura = None):
    coordinacionesAsignatura = Coordinacion_Docente.objects.filter(id_coordinacion__id_asignatura__id = idAsignatura).distinct('id_coordinacion')
    serializer = DocenteCursoSerializer(coordinacionesAsignatura, many = "true")
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
    ## Coordinaciones disponibles
    coordinaciones = Solicitud_Revision.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__id = idAsignatura).values_list('id_evaluacion__id_coordinacion__coordinacion',flat= True).distinct()
    ## Secciones disponibles
    secciones = Solicitud_Revision.objects.filter(id_evaluacion__id_coordinacion__id_asignatura__id = idAsignatura).values_list('id_evaluacion__id_coordinacion__seccion',flat= True).distinct()
    return Response([serializer.data,coordinaciones,secciones])
    
@api_view(['GET'])
def getAllEvaluaciones(request, idCoordinacion = None):
    evaluacionCoordinacion = Evaluacion.objects.filter(id_coordinacion__id = idCoordinacion).all()
    serializer = EvaluacionEspecificaSerializer(evaluacionCoordinacion, many = "true")
    return Response(serializer.data)

@api_view(['GET'])
def getEvaluacionesPorNombre(request, nombreEvaluacion = None, idAsignatura = None):
    evaluaciones = Evaluacion.objects.filter(id_coordinacion__id_asignatura__id = idAsignatura, nombre = nombreEvaluacion).all()
    serializer = EvaluacionEspecificaSerializer(evaluaciones, many = "true")
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
    solicitudes = Solicitud_Revision.objects.filter(id_docente__id = idDocente).order_by('fecha_creacion')
    serializer = SolicitudSerializer(solicitudes, many="true")
    return Response(serializer.data)

@api_view(['GET'])
def getCalificaionesByDocente(request,  idEvaluacion):
    calificaciones = Calificacion.objects.filter(id_evaluacion__id = idEvaluacion).all().order_by('id_estudiante__rut')
    serializer = CalificacionSerializer(calificaciones, many = "true")
    return Response(serializer.data)

@api_view(['PUT'])
def updateCalificacion(request, idCalificacion):
    calificacion = Calificacion.objects.get(id = idCalificacion)
    calificacion_actualizada = CalificacionEspecificaSerializer(calificacion, data = request.data)
    if calificacion_actualizada.is_valid():
        calificacion_actualizada.save()
        return Response(calificacion_actualizada.data)
    return Response(calificacion_actualizada.errors)

@api_view(['GET','POST'])
def addCambioNota(request, idAsignatura = None):
    
    if request.method == 'GET':
        ## Devolver los cambios
        cambios = Cambio_nota.objects.all()
        serializer = CambioNotaSerializer(cambios, many = "true")
        ## Coordinaciones disponibles
        #coordinaciones = Cambio_nota.objects.values_list('id_calificacion__id_evaluacion__id_coordinacion__coordinacion',flat= True).distinct()
        ## Secciones disponibles
        #secciones = Cambio_nota.objects.values_list('id_calificacion__id_evaluacion__id_coordinacion__seccion',flat= True).distinct()
        #return Response([serializer.data,coordinaciones, secciones])
        return Response(serializer.data)

    if request.method == 'POST':
        CambioAgregado = CambioNotaEspecificaSerializer(data = request.data)
        if CambioAgregado.is_valid():
            CambioAgregado.save()
            return Response(CambioAgregado.data)
        return Response(CambioAgregado.errors)

# obtener los cambios segun una asignatura
@api_view(['GET'])
def getCambioNota_idAsignatura(request,idAsignatura = None):
    
    if request.method == 'GET':
        ## Devolver los cambios 
        cambios = Cambio_nota.objects.filter(id_calificacion__id_evaluacion__id_coordinacion__id_asignatura__id = idAsignatura)
        serializer = CambioNotaSerializer(cambios, many = "true")
        ## Coordinaciones disponibles
        coordinaciones = Cambio_nota.objects.filter(id_calificacion__id_evaluacion__id_coordinacion__id_asignatura__id = idAsignatura).values_list('id_calificacion__id_evaluacion__id_coordinacion__coordinacion',flat= True).distinct()
        ## Secciones disponibles
        secciones = Cambio_nota.objects.filter(id_calificacion__id_evaluacion__id_coordinacion__id_asignatura__id = idAsignatura).values_list('id_calificacion__id_evaluacion__id_coordinacion__seccion',flat= True).distinct()
        return Response([serializer.data,coordinaciones, secciones])

@api_view(['POST'])
def cambioFechaCalificacion(request):
    cambioFecha = CambioFechaSerializer(data = request.data)
    if cambioFecha.is_valid():
        cambioFecha.save()
        return Response(cambioFecha.data)
    return Response(cambioFecha.errors)

@api_view(['GET'])
def getCambiosFecha(request):
    cambiosFecha = Cambio_Fecha.objects.all()
    serializer = CambioFechaDashboardSerializer(cambiosFecha, many="true")
    return Response(serializer.data)

##Falta un filter para que solo muestre los cambios del semestre actual
@api_view(['GET'])
def getCambiosNota(request):
    cambiosNota = Cambio_nota.objects.all()
    serializer = CambioNotaDashboardSerializer(cambiosNota, many="true")
    return Response(serializer.data)