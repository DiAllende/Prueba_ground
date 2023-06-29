from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from registro.models import UsersRegistro
from registro.forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar si el usuario existe en la base de datos
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireccionar utilizando el nombre de la URL

    form = RegisterForm()
    return render(request, 'login/login.html', {'form': form})


