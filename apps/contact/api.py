# apps/contact/api.py

from django.http import FileResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# --- NUEVOS IMPORTS PARA ARREGLAR SWAGGER ---
from drf_spectacular.utils import extend_schema, OpenApiTypes

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


# -------------------------------------------------------------------
# ViewSet #2: Solo para la gestión del CV
# -------------------------------------------------------------------
class CVDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listar y descargar documentos de CV.
    """
    queryset = CVDocument.objects.all().order_by('-uploaded_at')
    serializer_class = CVDocumentSerializer
    permission_classes = [AllowAny]

    # --- AQUI ESTA EL ARREGLO ---
    @extend_schema(
        # Le decimos a Swagger: "La respuesta es un archivo binario (PDF), no intentes leer JSON"
        responses={
            (200, 'application/pdf'): OpenApiTypes.BINARY
        },
        description="Descarga el último CV disponible."
    )
    @action(
        detail=False,
        methods=['get'],
        url_path='download-latest',
        renderer_classes=[PassthroughRenderer]
    )
    def download_latest(self, request):
        """
        Endpoint para descargar el CV más reciente.
        """
        latest_cv = self.get_queryset().first()
        
        if latest_cv:
            # Aseguramos que el archivo exista antes de abrirlo
            if not latest_cv.cv_file:
                return Response({"error": "File not found on server."}, status=404)

            response = FileResponse(
                latest_cv.cv_file.open('rb'),
                as_attachment=True,
                filename=latest_cv.cv_file.name.split('/')[-1]
            )
            return response
        
        return Response({"error": "No CV file has been uploaded."}, status=404)