from django.db import models

# Create your models here.
class UsersRegistro(models.Model):
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    password = models.CharField(verbose_name="Password", max_length=200)
    nombre = models.CharField(verbose_name="Nombre completo", max_length=200)
    rut= models.CharField(verbose_name="Rut", max_length=200)
    direccion= models.CharField(verbose_name="Direccion", max_length=200, blank=True, null=True)
    pais= models.CharField(verbose_name="Pais", max_length=100)
    cp= models.IntegerField(verbose_name="Codigo postal", blank=True, null=True)
    admin= models.BooleanField(verbose_name="Administrador", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "User Registrado"
        verbose_name_plural = "Users registrados"
        ordering = ['created']
    
    def __str__(self):
        return self.nombre
