from rest_framework import viewsets, mixins
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

class ContactSubmissionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint que solo permite crear (POST) nuevos envíos de contacto.
    No permite listar, actualizar o eliminar.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer