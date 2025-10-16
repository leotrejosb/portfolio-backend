from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Déjalo en blanco para que se genere automáticamente")
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    challenge = models.TextField()
    solution = models.TextField()
    image = models.URLField(max_length=500, help_text="URL de la imagen del proyecto")
    demo_url = models.URLField(max_length=500, blank=True, null=True)
    github_url = models.URLField(max_length=500, blank=True, null=True)
    
    technologies = models.ManyToManyField(Technology, related_name="projects")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at']


class Result(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="results")
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description