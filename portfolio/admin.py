# portfolio/admin.py

from django.contrib import admin
from .models import Project

# Registra el modelo Project en el sitio de administración
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Muestra estos campos en la lista de proyectos
    list_display = ('title', 'slug')
    # Pre-rellena automáticamente el campo 'slug' basándose en el título
    prepopulated_fields = {'slug': ('title',)}