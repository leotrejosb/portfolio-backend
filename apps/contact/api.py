# apps/contact/api.py

from django.http import FileResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated # 👈 Importa IsAuthenticated si lo necesitas
from rest_framework.response import Response

from .models import ContactSubmission, CVDocument # 👈 Importa CVDocument
from .serializers import ContactSubmissionSerializer

class ContactSubmissionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint para envíos de contacto y descarga de CV.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    # 👇 AÑADE ESTA ACCIÓN PERSONALIZADA DENTRO DE LA CLASE 👇
    @action(
        detail=False,
        methods=['get'],
        permission_classes=[AllowAny], # 🛡️ CAMBIA A [IsAuthenticated] PARA PROTEGERLO
        url_path='download-cv'
        renderer_classes=[PassthroughRenderer] # Use the new renderer here
    )
    def download_cv(self, request):
        """
        Endpoint seguro para descargar el CV desde la base de datos.
        """
        try:
            cv_document = CVDocument.objects.latest('uploaded_at')
            return FileResponse(
                cv_document.cv_file.open('rb'),
                as_attachment=True,
                filename=cv_document.cv_file.name.split('/')[-1]
            )
        except CVDocument.DoesNotExist:
            return Response({"error": "El archivo CV no fue encontrado."}, status=404)
        except Exception:
            return Response({"error": "Ocurrió un error al procesar el archivo."}, status=500)