# apps/contact/api.py

from django.http import FileResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Importaciones necesarias para ambos ViewSets
from .renderers import PassthroughRenderer
from .models import ContactSubmission, CVDocument
from .serializers import ContactSubmissionSerializer, CVDocumentSerializer

# -------------------------------------------------------------------
# ViewSet #1: Solo para el Formulario de Contacto
# -------------------------------------------------------------------
class ContactSubmissionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint que solo permite crear (POST) nuevos envíos de contacto.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    # La acción de descarga ha sido movida al CVDocumentViewSet para mantener el código limpio.


# -------------------------------------------------------------------
# ViewSet #2: Solo para la gestión del CV
# -------------------------------------------------------------------
class CVDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listar y descargar documentos de CV.
    """
    queryset = CVDocument.objects.all().order_by('-uploaded_at')
    serializer_class = CVDocumentSerializer
    permission_classes = [AllowAny] # Puedes cambiarlo a IsAuthenticated si lo necesitas

    @action(
        detail=False,
        methods=['get'],
        url_path='download-latest',
        renderer_classes=[PassthroughRenderer] # Usa el renderizador para archivos
    )
    def download_latest(self, request):
        """
        Endpoint para descargar el CV más reciente.
        """
        latest_cv = self.get_queryset().first() # Obtenemos el primero (más reciente)
        
        if latest_cv:
            response = FileResponse(
                latest_cv.cv_file.open('rb'),
                as_attachment=True,
                filename=latest_cv.cv_file.name.split('/')[-1]
            )
            return response
        
        return Response({"error": "No CV file has been uploaded."}, status=404)