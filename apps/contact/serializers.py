from rest_framework import serializers
from .models import ContactSubmission, CVDocument

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']

class CVDocumentSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo CVDocument.
    """
    # Hacemos que el campo del archivo devuelva la URL completa para ser consumida fácilmente.
    cv_file_url = serializers.FileField(source='cv_file', read_only=True)

    class Meta:
        model = CVDocument
        # Define los campos que quieres exponer en la API
        fields = ['id', 'name', 'uploaded_at', 'cv_file_url']
        read_only_fields = fields # Hacemos todos los campos de solo lectura