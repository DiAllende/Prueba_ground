from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
]