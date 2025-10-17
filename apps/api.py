from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contact.api import ContactSubmissionViewSet, CVDocumentViewSet
from apps.portfolio.api import ProjectViewSet, TechnologyViewSet


router = DefaultRouter()
router.register(r'contact', ContactSubmissionViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'technologies', TechnologyViewSet)
router.register(r'documents', CVDocumentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]