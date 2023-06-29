from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login/login.html'), name="login"),
    path('login/', LogoutView.as_view(template_name='login/logout.html'), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)