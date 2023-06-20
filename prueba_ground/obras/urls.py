from django.contrib import admin
from django.urls import path
from obras import views
from prueba_ground import settings

urlpatterns = [
    path('obras/', views.obras, name="obras"),
    path('obras/<int:pk>/', views.detalle_obra, name='details_obra'),
    path('crear/', views.crear_elemento, name='crear_elemento'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)