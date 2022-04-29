from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
from .choices import COMPONENTES_CHOICES, ESTADOS_CHOICES, ESTADOS_EVALUACION_CHOICES, SEMESTRES_CHOICES, TIPO_OBS_CHOICES

# Create your models here.

# Modelos heredables - Clases abstractas.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 40, null = True)
    apellido = models.CharField(max_length=40, null = True)
    rut = models.PositiveIntegerField(null= True)
    dig_verificador = models.CharField(max_length=1, null = True)
    email = models.EmailField(max_length=254, null = True)
    password = models.CharField(max_length=30, null = True)

    class Meta:
        abstract = True

class Tipos(models.Model):
    nombre = models.CharField(max_length = 40)

    class Meta:
        abstract = True

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

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
    nombre = models.CharField(max_length = 100, null = False)
    siglas = models.CharField(max_length = 10, null = True)
    id_vicedecano = models.ForeignKey(Vicedecano_Docencia, null = False, on_delete = models.CASCADE)

class Departamento(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    id_subdirector = models.ForeignKey(Subdirector_Docente, null = False, on_delete = models.CASCADE)
    id_vicedecano = models.ForeignKey(Vicedecano_Docencia, null = False, on_delete = models.CASCADE)

class Carrera(models.Model):
    nombre = models.CharField(max_length = 100, null = False)
    id_jefeCarrera = models.ForeignKey(Jefe_Carrera, null = False, on_delete = models.CASCADE)
    id_departamento = models.ForeignKey(Departamento, null = False, on_delete = models.CASCADE)

class Plan_Estudio(models.Model):
    codigo = models.CharField(max_length = 10)
    year_crecion = models.CharField(max_length = 4, validators = [MinLengthValidator(4)])
    codigo = models.CharField(max_length = 10, unique = False)
    id_carrera = models.ForeignKey(Carrera, null = False, on_delete = models.CASCADE)

class Tipo_Asignatura(Tipos):
    pass

class Asignatura(models.Model):
    nombre = models.CharField(max_length = 40, null = False)
    codigo = models.CharField(max_length = 20, unique = True, null = False)
    nivel = models.PositiveSmallIntegerField
    componente = models.CharField(max_length = 1, choices = COMPONENTES_CHOICES, null = False)
    isMBI = models.BooleanField(null = False)
    isAutogestionada = models.BooleanField(null = False)
    id_tipoAsignatura = models.ForeignKey(Tipo_Asignatura, null = False, on_delete = models.CASCADE)
    id_coordinador = models.ForeignKey(Coordinador, null = False, on_delete = models.CASCADE)

class Asignaturas_PlanEstudio(models.Model):
    id_asignatura = models.ForeignKey(Asignatura, null = False, on_delete = models.CASCADE)
    id_planEstudio = models.ForeignKey(Plan_Estudio, null = False, on_delete = models.CASCADE)

class Semestre(models.Model):
    year = models.PositiveSmallIntegerField
    semestre = models.IntegerField(choices = SEMESTRES_CHOICES)
    isActual = models.BooleanField

class Coordinacion_Seccion(models.Model):
    coordinacion = models.CharField(max_length = 1, null = False)
    seccion = models.PositiveSmallIntegerField(null = False)
    isActive = models.BooleanField(null = False)
    bloques_horario = models.CharField(max_length = 16, null = False)
    id_semetre = models.ForeignKey(Semestre, null = False, on_delete = models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, null = False, on_delete = models.CASCADE)

class Estadistica_Curso(TimeStampMixin):
    promedio_general = models.DecimalField(max_digits = 4, decimal_places = 3)
    mejor_nota = models.DecimalField(max_digits = 4, decimal_places = 3)
    peor_nota = models.DecimalField(max_digits = 4, decimal_places = 3)
    desviacionEstandar = models.DecimalField(max_digits = 4, decimal_places = 3)
    id_coordinacion = models.ForeignKey(Coordinacion_Seccion, null = False, on_delete = models.CASCADE)

class Coordinacion_Docente(models.Model):
    id_docente = models.ForeignKey(Docente, null = False, on_delete = models.CASCADE)
    id_coordinacion = models.ForeignKey(Coordinacion_Seccion, null = False, on_delete = models.CASCADE)
    
class Estudiante(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    id_semestreIngreso = models.ForeignKey(Semestre, null = True, on_delete = models.CASCADE)

class Coordinacion_Estudiante(models.Model):
    promedioEstudiante = models.DecimalField(max_digits = 4, decimal_places = 3)
    id_estudiante = models.ForeignKey(Estudiante, null = False, on_delete = models.CASCADE)
    id_coordinacion = models.ForeignKey(Coordinacion_Seccion, null = False, on_delete = models.CASCADE)
    
class Tipo_Evaluacion(Tipos):
    pass

class Observacion(models.Model):
    contenido = models.TextField(null = True)
    archivoAdjunto = models.FileField(null = True)
    tipo = models.CharField(max_length = 1, choices = TIPO_OBS_CHOICES)

class Evaluacion(models.Model):
    nombre = models.CharField(max_length = 40, null = False)
    fechaEvActual = models.DateField(input_formats = settings.DATE_INPUT_FORMATS, null = False)
    fechaEntrega = models.DateField(input_formats = settings.DATE_INPUT_FORMATS, null = False)
    ponderacion = models.DecimalField(max_digits = 2, decimal_places = 1, null = False)
    estado = models.CharField(max_length = 1, choices = ESTADOS_EVALUACION_CHOICES, null = False)
    id_tipoEvaluacion = models.ForeignKey(Tipo_Evaluacion, null = True, on_delete = models.CASCADE)
    id_docente = models.ForeignKey(Docente, null = False, on_delete = models.CASCADE)
    id_observacion = models.ForeignKey(Observacion, null = True, on_delete = models.CASCADE)

class Mensaje(models.Model):
    contenido = models.TextField
    fecha = models.DateField(auto_now = True, auto_now_add = False)
    estado = models.CharField(max_length = 1, choices = ESTADOS_CHOICES)