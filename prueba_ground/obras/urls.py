from django.contrib import admin
from django.urls import path
from core.views import ObrasListView
from obras import views
from prueba_ground import settings

urlpatterns = [
    path('obras/<int:pk>/', views.detalle_obra, name='details_obra'),
    path('obras/', views.obras, name='obras'),
    path('crear/', views.crear_elemento, name='crear_elemento'),
    path('obras/<int:pk>/update/', views.update_obra, name='update_obra'),
    path('borrar/<int:pk>/', views.borrar_obra, name='borrar_obra'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)