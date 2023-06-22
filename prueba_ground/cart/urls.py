from django.urls import path

from prueba_ground import settings
from .views import  actualizar_cantidad, agregar_al_carrito, eliminar_del_carrito, limpiar_carrito, ver_carrito

urlpatterns = [
    path('add/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', ver_carrito, name='ver_carrito'),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),
    path('cart/eliminar/<int:obra_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('cart/obras/actualizar/<int:obra_id>/', actualizar_cantidad, name='actualizar_cantidad'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)