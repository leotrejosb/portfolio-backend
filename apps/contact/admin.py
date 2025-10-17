from django.contrib import admin
from .models import ContactSubmission, CVDocument

# -------------------------------------------------------------------
# Clase de Admin para los envíos del formulario de contacto (sin cambios)
# -------------------------------------------------------------------
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    """
    Personaliza la vista del admin para los envíos de contacto.
    """
    list_display = ('subject', 'name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

# -------------------------------------------------------------------
# 👇 NUEVA Clase de Admin para gestionar los documentos de CV 👇
# -------------------------------------------------------------------
@admin.register(CVDocument)
class CVDocumentAdmin(admin.ModelAdmin):
   list_display = ('name', 'cv_file', 'uploaded_at')
    readonly_fields = ('uploaded_at',)