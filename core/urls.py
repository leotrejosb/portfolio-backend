# core/urls.py

from django.contrib import admin
from django.urls import path, include
# Importaciones necesarias para la documentación
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Tu API principal
    path('api/', include('portfolio.urls')),

    # --- RUTAS DE DOCUMENTACIÓN ---
    # Genera el archivo schema.yml que describe tu API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Interfaz de Swagger UI (la más común y útil)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Interfaz de Redoc (una alternativa más limpia)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]