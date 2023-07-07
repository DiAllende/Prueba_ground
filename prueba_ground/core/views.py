from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from obras.models import Obras
from django.shortcuts import render
from registro.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from registro.forms import CustomUserEditForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

# Create your views here.
def index(request):
    obras = Obras.objects.all()[:4]  # Obtén las primeras 3 obras
    return render(request, "core/home.html", {'obras': obras})

def ventas_especiales(request):
    return render(request, "core/VE.html")


def detalles_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    return render(request, 'obras/detalles_obra.html', {'obra': obra})

class ObrasListView(ListView):
    model = Obras
    template_name = 'obras/obras.html'
    context_object_name = 'obras'

@user_passes_test(lambda user: user.email == 'pruebamailsnoreply@gmail.com', login_url='404')
def registered_users(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'core/usuarios/Lista_usuarios.html', {'usuarios': usuarios})


@user_passes_test(lambda user: user.email == 'pruebamailsnoreply@gmail.com', login_url='404')
def editar_usuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('registered_users')
    else:
        form = CustomUserEditForm(instance=usuario)

    return render(request, 'core/usuarios/editar_usuario.html', {'form': form})


@user_passes_test(lambda user: user.email == 'pruebamailsnoreply@gmail.com', login_url='404')
def borrar_usuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('registered_users')

    return render(request, 'core/usuarios/eliminar_usuario.html', {'usuario': usuario})