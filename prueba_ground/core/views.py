from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/home.html")

def carrito(request):
    return render(request, "core/carrito.html")


