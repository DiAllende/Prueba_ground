from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from obras.form import CreateObraForm, UpdateObraForm
from prueba_ground import settings
from .models import Obras
from cart.views import agregar_al_carrito, ver_carrito
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

def obras(request):
    obras = Obras.objects.all()
    return render(request, "obras/obras.html", {'obras': obras})

def crear_elemento(request):
    if request.method == 'POST':
        form = CreateObraForm(request.POST, request.FILES)
        if form.is_valid():
            obra = form.save()

            # Construye la URL de la vista 'aprobar_obra' con el argumento 'obra_id'
            aprobar_url = request.build_absolute_uri(reverse('aprobar_obra', args=[obra.id]))
            rechazar_url = request.build_absolute_uri(reverse('rechazar_obra', args=[obra.id]))

            # Envío de notificación o correo electrónico al administrador
            subject = 'Solicitud de Aprobación de Obra'
            html_content = render_to_string('obras/email/aprobacion_obra.html', {'obra': obra, 'approve_url': aprobar_url, 'reject_url': rechazar_url, 'SITE_URL': settings.SITE_URL})
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(subject, text_content, 'pruebamailsnoreply@gmail.com', ['pruebamailsnoreply@gmail.com'])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            return redirect('obras')
    else:
        form = CreateObraForm()

    return render(request, 'obras/create_obra.html', {'form': form})

def detalle_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    return render(request, 'obras/details_obra.html', {'obra': obra})


def is_admin(user):
    return user.is_authenticated and user.admin

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
def borrar_obra(request, pk):
    obra = get_object_or_404(Obras, pk=pk)
    obra.delete()
    return redirect('obras')

def aprobar_obra(request, obra_id):
    if request.user.email != 'pruebamailsnoreply@gmail.com':
        return HttpResponseForbidden('Acceso denegado')  # Devuelve un error 403 Forbidden si el remitente no es válido

    obra = get_object_or_404(Obras, id=obra_id)
    obra.estado = 'aprobada'
    obra.save()
    # Otras acciones que desees realizar después de aprobar la obra
    return redirect('obras')


def rechazar_obra(request, obra_id):
    if request.user.email != 'pruebamailsnoreply@gmail.com':
        return HttpResponseForbidden('Acceso denegado')  # Devuelve un error 403 Forbidden si el remitente no es válido

    obra = get_object_or_404(Obras, id=obra_id)
    obra.estado = 'rechazada'
    obra.delete()
    # Otras acciones que desees realizar después de rechazar la obra
    return redirect('obras')
