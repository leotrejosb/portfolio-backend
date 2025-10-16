# portfolio/models.py

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Project(models.Model):
    # Campos de texto básicos
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="Versión amigable para URL del título, ej: mi-primer-proyecto")
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    challenge = models.TextField()
    solution = models.TextField()

    # Campos de tipo Array (lista). Estos requieren PostgreSQL.
    results = ArrayField(models.CharField(max_length=200), blank=True)
    technologies = ArrayField(models.CharField(max_length=50), blank=True)

    # Campos de URL
    image = models.URLField(max_length=500)
    demo_url = models.URLField(max_length=500, blank=True, null=True)
    github_url = models.URLField(max_length=500, blank=True, null=True)

    # Esto ayuda a que los proyectos se muestren de forma legible en el panel de admin
    def __str__(self):
        return self.title