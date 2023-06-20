from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from obras.models import Obras

# Create your views here.
def index(request):
    obras = Obras.objects.all()[:3]  # Obtén las primeras 3 obras
    return render(request, "core/home.html", {'obras': obras})

def carrito(request):
    return render(request, "core/carrito.html")

def detalles_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    return render(request, 'obras/detalles_obra.html', {'obra': obra})

class ObrasListView(ListView):
    model = Obras
    template_name = 'core/home.html'
    context_object_name = 'obras'