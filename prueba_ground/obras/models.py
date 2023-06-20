from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Obras(models.Model):
    Nombre = models.CharField(verbose_name="Nombre", max_length=100, unique=True)
    Precio = models.IntegerField(verbose_name="Precio")
    Autor = models.CharField(verbose_name="Nombre Autor", max_length=200)
    Titulo_Original= models.CharField(verbose_name="Titulo Original", max_length=200)
    Tecnica = models.CharField(verbose_name="Tecnica", max_length=200, blank=True, null=True)
    Anio = models.IntegerField(verbose_name="Año")
    Detalles_obra = models.TextField(verbose_name="Detalle Obra", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="Services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
        ordering = ['created']
    
    def __str__(self):
        return self.Nombre
