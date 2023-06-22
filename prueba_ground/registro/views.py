from django.shortcuts import render, redirect
from .forms import RegisterForm

def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el formulario en la base de datos
            return redirect('login')  # Redirigir a una página de éxito
    else:
        form = RegisterForm()
    

    return render(request, 'registro/registro.html', {'form': form})
