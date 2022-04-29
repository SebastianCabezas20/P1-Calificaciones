from asyncio.windows_events import NULL
from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
from .choices import COMPONENTES_CHOICES, ESTADOS_EVALUACION_CHOICES, ESTADOS_SOLICITUD_CHOICES, SEMESTRES_CHOICES, TIPO_OBS_CHOICES

# Create your models here.

# Modelos heredables - Clases abstractas.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 40, blank = True)
    apellido = models.CharField(max_length = 40, blank = True)
    rut = models.PositiveIntegerField(blank = False)
    dig_verificador = models.CharField(max_length = 1, blank = False)
    email = models.EmailField(max_length = 254, blank = False)
    password = models.CharField(max_length = 30, blank = False)

    class Meta:
        abstract = True

class Tipos(models.Model):
    nombre = models.CharField(max_length = 40)

    class Meta:
        abstract = True

# -----------------------------------------------------------------------------

class Vicedecano_Docencia(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Subdirector_Docente(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Jefe_Carrera(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Docente(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Coordinador(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Facultad(models.Model):
    nombre = models.CharField(max_length = 100, blank = False)
    siglas = models.CharField(max_length = 10, blank = True)
    id_vicedecano = models.ForeignKey(Vicedecano_Docencia, blank = False , null = False, on_delete = models.CASCADE)

class Departamento(models.Model):
    nombre = models.CharField(max_length = 50, blank = False)
    id_subdirector = models.ForeignKey(Subdirector_Docente, blank = False , null = False, on_delete = models.CASCADE)
    id_vicedecano = models.ForeignKey(Vicedecano_Docencia, blank = False, null = False, on_delete = models.CASCADE)

class Carrera(models.Model):
    nombre = models.CharField(max_length = 100, blank = False)
    id_jefeCarrera = models.ForeignKey(Jefe_Carrera, blank = False, null = False, on_delete = models.CASCADE)
    id_departamento = models.ForeignKey(Departamento, blank = False, null = False, on_delete = models.CASCADE)

class Plan_Estudio(models.Model):
    codigo = models.CharField(max_length = 10, blank = False, unique = True)
    year_crecion = models.CharField(max_length = 4, validators = [MinLengthValidator(4)])
    id_carrera = models.ForeignKey(Carrera, blank = False, null = False, on_delete = models.CASCADE)

class Tipo_Asignatura(Tipos):
    pass

class Asignatura(models.Model):
    nombre = models.CharField(max_length = 40, blank = False)
    codigo = models.CharField(max_length = 20, unique = True, blank = False)
    nivel = models.PositiveSmallIntegerField(blank = True, null = True)
    componente = models.CharField(max_length = 1, choices = COMPONENTES_CHOICES, blank = False)
    isMBI = models.BooleanField
    isAutogestionada = models.BooleanField
    id_tipoAsignatura = models.ForeignKey(Tipo_Asignatura, blank = False, null = False, on_delete = models.CASCADE)
    id_coordinador = models.ForeignKey(Coordinador, blank = False, null = False, on_delete = models.CASCADE)

class Asignaturas_PlanEstudio(models.Model):
    id_asignatura = models.ForeignKey(Asignatura, blank = False, null = False, on_delete = models.CASCADE)
    id_planEstudio = models.ForeignKey(Plan_Estudio, blank = False, null = False, on_delete = models.CASCADE)

class Semestre(models.Model):
    year = models.PositiveSmallIntegerField
    semestre = models.IntegerField(choices = SEMESTRES_CHOICES)
    isActual = models.BooleanField

class Coordinacion_Seccion(models.Model):
    coordinacion = models.CharField(max_length = 1, blank = False)
    seccion = models.PositiveSmallIntegerField(blank = False)
    isActive = models.BooleanField
    bloques_horario = models.CharField(max_length = 16, blank = False)
    id_semetre = models.ForeignKey(Semestre, null = False, on_delete = models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, null = False, on_delete = models.CASCADE)

class Estadistica_Curso(models.Model):
    promedio_general = models.DecimalField(max_digits = 4, decimal_places = 3)
    mejor_nota = models.DecimalField(max_digits = 4, decimal_places = 3)
    peor_nota = models.DecimalField(max_digits = 4, decimal_places = 3)
    desviacionEstandar = models.DecimalField(max_digits = 4, decimal_places = 3)
    id_coordinacion = models.ForeignKey(Coordinacion_Seccion, null = False, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)

class Coordinacion_Docente(models.Model):
    id_docente = models.ForeignKey(Docente, null = False, on_delete = models.CASCADE)
    id_coordinacion = models.ForeignKey(Coordinacion_Seccion, null = False, on_delete = models.CASCADE)
    
class Estudiante(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = False)
    id_semestreIngreso = models.ForeignKey(Semestre, on_delete = models.CASCADE, null = False)

class Coordinacion_Estudiante(models.Model):
    promedioEstudiante = models.DecimalField(max_digits = 4, decimal_places = 3, null = True)
    id_estudiante = models.ForeignKey(Estudiante, null = False, on_delete = models.CASCADE)
    id_coordinacion = models.ForeignKey(Coordinacion_Seccion, null = False, on_delete = models.CASCADE)
    
class Tipo_Evaluacion(Tipos):
    pass

class Observacion(models.Model):
    contenido = models.TextField(blank = True)
    archivoAdjunto = models.FileField(null = True)
    tipo = models.CharField(max_length = 1, choices = TIPO_OBS_CHOICES, blank = False)

class Evaluacion(models.Model):
    nombre = models.CharField(max_length = 40, blank = False)
    fechaEvActual = models.DateField(null = False)
    fechaEntrega = models.DateField(null = False)
    ponderacion = models.DecimalField(max_digits = 2, decimal_places = 1, null = False)
    estado = models.CharField(max_length = 1, choices = ESTADOS_EVALUACION_CHOICES, blank = False)
    id_tipoEvaluacion = models.ForeignKey(Tipo_Evaluacion, null = True, on_delete = models.CASCADE)
    id_docente = models.ForeignKey(Docente, null = False, on_delete = models.CASCADE)
    id_observacion = models.ForeignKey(Observacion, null = True, on_delete = models.CASCADE)

class Cambio_Ponderacion(models.Model):
    ponderacionAnterior = models.DecimalField(max_digits = 4, decimal_places = 3, null = False)
    ponderacionNueva = models.DecimalField(max_digits = 4, decimal_places = 3, null = False)
    motivo = models.TextField(blank = False)
    id_evaluacion = models.ForeignKey(Evaluacion, null = False, on_delete = models.CASCADE)

class Cambio_Fecha(models.Model):
    fechaAnterior = models.DateField(null = False)
    fechaNueva = models.DateField(null = False)
    motivo = models.TextField(blank = False)
    id_evaluacion = models.ForeignKey(Evaluacion, null = False, on_delete = models.CASCADE)

class Solicitud_Revision(models.Model):
    motivo = models.TextField(blank = False)
    fecha_creacion = models.DateTimeField(null = False)
    archivoAdjunto = models.FileField(null = True)
    respuesta = models.TextField(blank = True, default = '')
    fecha_respuesta = models.DateTimeField(null = True, default = NULL)
    estado = models.CharField(max_length = 1, choices = ESTADOS_SOLICITUD_CHOICES, blank = False, default = '')
    id_estudiante = models.ForeignKey(Estudiante, null = False, on_delete = models.CASCADE)
    id_docente = models.ForeignKey(Docente, null = False, on_delete = models.CASCADE)
    id_evaluacion = models.ForeignKey(Evaluacion, null = False, on_delete = models.CASCADE)