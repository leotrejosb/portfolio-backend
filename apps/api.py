from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contact.api import ContactSubmissionViewSet
from apps.portfolio.api import ProjectViewSet, TechnologyViewSet


router = DefaultRouter()
router.register(r'contact', ContactSubmissionViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'technologies', TechnologyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]