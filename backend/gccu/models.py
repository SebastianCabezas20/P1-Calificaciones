from pickle import TRUE
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40, null=True)
    apellido = models.CharField(max_length=40, null=True)
    rut = models.PositiveIntegerField(null= True)
    dig_verificador = models.CharField(max_length=1, null=True)
    email = models.EmailField(max_length=254, null=TRUE)
    password = models.CharField(max_length=30, null=True)