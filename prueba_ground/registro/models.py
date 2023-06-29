from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=150, unique=False)
    rut = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    cp = models.CharField(max_length=10)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    # Especificar el related_name para evitar conflictos con los modelos User y Group
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
