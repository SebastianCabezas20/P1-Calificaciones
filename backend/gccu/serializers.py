from dataclasses import field
from rest_framework import serializers
from .models import *

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion      
        fields = '__all__'  

