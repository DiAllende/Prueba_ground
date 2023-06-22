from django.http import JsonResponse
from django.shortcuts import redirect, render
from .cart import Cart
from django.views.decorators.http import require_POST

from obras.models import Obras

def carrito(request):
    return render(request, "cart/carrito.html")

def agregar_al_carrito(request):
    if request.method == 'POST':
        obra_id = request.POST.get('obra_id')
        
        try:
            obra = Obras.objects.get(id=obra_id)
        except Obras.DoesNotExist:
            response_data = {'success': False, 'message': 'La obra no existe'}
            return JsonResponse(response_data, status=404)
        
        cart = Cart(request)
        cart.agregar(obra)
        
        response_data = {'success': True, 'message': 'Obra agregada al carrito correctamente'}
        return redirect('ver_carrito')
    else:
        response_data = {'success': False, 'message': 'Método no permitido'}
        return JsonResponse(response_data, status=405)

def ver_carrito(request):
    cart = Cart(request)
    obras_en_carrito = cart.get_obras()
    total = cart.get_total()
    
    for item in obras_en_carrito:
        obra_data = item['obra']
        obra = Obras()
        obra.id = obra_data.id
        obra.Nombre = obra_data.Nombre
        obra.image = obra_data.image
        obra.Precio = obra_data.Precio
        item['obra'] = obra
    
    return render(request, 'cart/ver_carrito.html', {'obras': obras_en_carrito, 'total': total})

def limpiar_carrito(request):
    cart = Cart(request)
    cart.limpiar()
    
    if not cart.get_obras():
        return redirect('obras') 
    return redirect('ver_carrito') 

def eliminar_del_carrito(request, obra_id):
    cart = Cart(request)
    obra_id = str(obra_id)
    if obra_id in cart.cart:
        cart.eliminar(obra_id)
    return redirect('ver_carrito')

@require_POST
def actualizar_cantidad(request, obra_id):
    cart = Cart(request)
    cantidad = int(request.POST['cantidad'])
    cart.actualizar_cantidad(obra_id, cantidad)
    return redirect('ver_carrito')