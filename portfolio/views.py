# portfolio/views.py
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

# Esta vista es para obtener la lista de TODOS los proyectos
class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Esta vista es para obtener UN solo proyecto usando su 'slug'
class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug' # Le dice a DRF que busque por el campo 'slug' en la URL