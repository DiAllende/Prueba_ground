from django.shortcuts import get_object_or_404, render
from obras.models import Obras
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, "core/home.html")

def carrito(request):
    return render(request, "core/carrito.html")

def detalles_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    return render(request, 'obras/detalles_obra.html', {'obra': obra})
