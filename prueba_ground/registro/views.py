from django.shortcuts import render, redirect

from registro.models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro/registro.html', {'form': form})


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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
                    print("Credenciales inválidas: " + email + ", " + password)
                    return redirect('login')  # Redirige de nuevo al formulario de inicio de sesión
            except CustomUser.DoesNotExist:
                messages.error(request, 'Credenciales inválidas.')
                print("Credenciales inválidas: " + email + ", " + password)
                return redirect('login')  # Redirige de nuevo al formulario de inicio de sesión
    else:
        form = LoginForm()
    
    return render(request, 'registro/login.html', {'form': form})
