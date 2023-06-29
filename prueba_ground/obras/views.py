from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from obras.form import CreateObraForm, UpdateObraForm
from .models import Obras
from cart.views import agregar_al_carrito, ver_carrito

def obras(request):
    obras = Obras.objects.all()
    return render(request, "obras/obras.html", {'obras': obras})

@login_required
def crear_elemento(request):
    if request.method == 'POST':
        form = CreateObraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('obras')
    else:
        form = CreateObraForm()

    return render(request, 'obras/create_obra.html', {'form': form})

def detalle_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    return render(request, 'obras/details_obra.html', {'obra': obra})

@login_required
def update_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)

    if request.method == 'POST':
        form = UpdateObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('details_obra', pk=pk)
    else:
        form = UpdateObraForm(instance=obra)

    return render(request, 'obras/update_obra.html', {'form': form})

@login_required
def borrar_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    obra.delete()
    return redirect('obras')



