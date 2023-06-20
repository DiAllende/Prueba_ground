from django.shortcuts import get_object_or_404, render, redirect

from obras.form import CreateObraForm
from .models import Obras
import os

def obras(request):
    obras = Obras.objects.all()
    return render(request, "obras/obras.html", {'obras': obras})

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