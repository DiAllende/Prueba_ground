from django.shortcuts import get_object_or_404, render, redirect
from .models import Obras
import os

def obras(request):
    obras = Obras.objects.all()
    return render(request, "obras/obras.html", {'obras': obras})

def crear_elemento(request):

    if request.method == 'POST':
        nombre= request.POST["nombre"]
        precio= request.POST["Precio"]
        nombre_autor= request.POST["nombre_autor"]
        titulo= request.POST["titulo"]
        tecnica= request.POST["tecnica"]
        anio= request.POST["anio"]
        detalle= request.POST["detalle"]
        imagen=request.POST["imagen"]
        #imagen = imagen.replace(" ","_")
        imagen_ruta = os.path.join("Services/", imagen)
        
        obj=Obras.objects.create(
            Nombre=nombre,
            Precio = precio,
            Autor = nombre_autor,
            Titulo_Original= titulo,
            Tecnica = tecnica,
            Anio = anio,
            Detalles_obra = detalle,
            image = imagen_ruta
            )
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
    else:
        return render(request, 'obras/create_obra.html')
    return render(request, 'obras/create_obra.html', context)

def detalle_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    return render(request, 'obras/details_obra.html', {'obra': obra})
