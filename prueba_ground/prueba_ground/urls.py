"""prueba_ground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('', views.index, name="home"),
    path('', include('registro.urls')),
    path('cart/', include('cart.urls')),
    path('', include('obras.urls')),
    path('admin/', admin.site.urls),
    path('obras/', views.ObrasListView.as_view(), name='obras'),
    path('ventas_especiales/', views.ventas_especiales, name='ve'),
    path('Lista_usuarios/', views.registered_users, name='registered_users'),    
    path('editar_usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('borrar_usuario/<int:pk>/', views.borrar_usuario, name='borrar_usuario'),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

