# portfolio/urls.py
from django.urls import path
from .views import ProjectListAPIView, ProjectDetailAPIView

urlpatterns = [
    # URL para la lista de proyectos: http://127.0.0.1:8000/api/projects/
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    
    # URL para un proyecto individual: http://127.0.0.1:8000/api/projects/mi-slug-de-proyecto/
    path('projects/<slug:slug>/', ProjectDetailAPIView.as_view(), name='project-detail'),
]