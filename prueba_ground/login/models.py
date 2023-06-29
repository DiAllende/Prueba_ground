from django.db import models
from registro.models import UsersRegistro
# Create your models here.

class Users(models.Model):
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    password = models.CharField(verbose_name="Password", max_length=200)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['created']
    
    def __str__(self):
        return self.email
