from django.contrib import admin
from django.urls import path
from core.views import ObrasListView
from obras import views
from prueba_ground import settings
from .views import agregar_al_carrito, ver_carrito

urlpatterns = [
    path('obras/<int:pk>/', views.detalle_obra, name='details_obra'),
    path('obras/', views.obras, name='obras'),
    path('obras/crear/', views.crear_elemento, name='crear_elemento'),
    path('obras/<int:pk>/update/', views.update_obra, name='update_obra'),
    path('obras/borrar/<int:pk>/', views.borrar_obra, name='borrar_obra'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)