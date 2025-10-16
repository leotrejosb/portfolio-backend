from rest_framework import serializers
from .models import Project, Technology, Result

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['description']

class ProjectSerializer(serializers.ModelSerializer):
    # Usamos StringRelatedField para obtener solo los nombres, como en tu mock
    technologies = serializers.StringRelatedField(many=True, read_only=True)
    results = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 'full_description',
            'challenge', 'solution', 'results', 'technologies', 'image',
            'demo_url', 'github_url'
        ]
        # Hacemos que el lookup en la API sea por slug en lugar de ID
        lookup_field = 'slug'