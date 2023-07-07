from django.shortcuts import render, redirect
from registro.models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from registro.models import CustomUser
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después de registrar al usuario
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro/registro.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Credenciales inválidas.')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Credenciales inválidas.')
        else:
            messages.error(request, 'Credenciales inválidas.')
    else:
        form = LoginForm()

    return render(request, 'registro/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated and isinstance(request.user, CustomUser):
        logout(request)
    return redirect('home')
