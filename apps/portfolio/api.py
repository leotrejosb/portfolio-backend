from rest_framework import viewsets
from .models import Project, Technology
from .serializers import ProjectSerializer, TechnologySerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los proyectos.
    - Lista todos los proyectos.
    - Obtiene un proyecto por su 'slug'.
    """
    queryset = Project.objects.all().prefetch_related('technologies', 'results')
    serializer_class = ProjectSerializer
    lookup_field = 'slug' # MUY IMPORTANTE para que funcione con /projects/[slug]

class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver las tecnologías.
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer