from django.contrib import admin
from .models import Project, Technology, Result

class ResultInline(admin.TabularInline):
    model = Result
    extra = 1  # Espacios para añadir nuevos resultados

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'created_at')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}  # Autocompleta el slug
    inlines = [ResultInline] # Permite añadir resultados directamente en el proyecto

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)