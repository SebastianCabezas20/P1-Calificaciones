from pickle import TRUE
from django.db import models
from django.core.validators import MinLengthValidator
from .choices import ESTADOS_CHOICES

# Create your models here.

# Modelos heredables - Clases abstractas.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 40, null=True)
    apellido = models.CharField(max_length=40, null=True)
    rut = models.PositiveIntegerField(null= True)
    dig_verificador = models.CharField(max_length=1, null=True)
    email = models.EmailField(max_length=254, null=TRUE)
    password = models.CharField(max_length=30, null=True)

    class Meta:
        abstract = True

class Tipos(models.Model):
    nombre = models.CharField(max_length = 40)

    class Meta:
        abstract = True

# -----------------------------------------------------------------------------

class Estudiante(Usuario):
    pass

class Mensaje(models.Model):
    contenido = models.TextField
    fecha = models.DateField(auto_now = True, auto_now_add = False)
    estado = models.CharField(max_length = 1, choices = ESTADOS_CHOICES)

class Tipo_Observacion(Tipos):
    pass

class Tipo_Evaluacion(Tipos):
    pass

class Estado_Evaluacion(Tipos):
    siglas = models.CharField(max_length = 5)

class Vicedecano_Docencia(Usuario):
    pass   

class Subdirector_Docente(Usuario):
    pass

class Jefe_Carrera(Usuario):
    pass

class Facultad(models.Model):
    nombre = models.CharField(max_length = 100)
    siglas = models.CharField(max_length = 10)
    id_vicedecano = models.ForeignKey(Vicedecano_Docencia, null = True, on_delete = models.CASCADE)

class Departamento(models.Model):
    nombre = models.CharField(max_length = 50)
    id_subdirector = models.ForeignKey(Subdirector_Docente, null = True, on_delete = models.CASCADE)
    id_vicedecano = models.ForeignKey(Vicedecano_Docencia, null = True, on_delete = models.CASCADE)

class Carrera(models.Model):
    nombre = models.CharField(max_length = 100)
    id_jefeCarrera = models.ForeignKey(Jefe_Carrera, null = True, on_delete = models.CASCADE)
    id_departamento = models.ForeignKey(Departamento, null = True, on_delete = models.CASCADE)

class Tipo_Asignatura(Tipos):
    pass

class Plan_Estudio(models.Model):
    codigo = models.CharField(max_length = 10)
    year_crecion = models.CharField(max_length = 4, validators = [MinLengthValidator(4)])
    id_carrera = models.ForeignKey(Carrera, null = True, on_delete = models.CASCADE)
