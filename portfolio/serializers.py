# portfolio/serializers.py
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # '__all__' traduce todos los campos de tu modelo a JSON
        fields = '__all__'