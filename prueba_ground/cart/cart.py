from decimal import Decimal
from django.conf import settings
from obras.models import Obras

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def agregar(self, obra, cantidad=1):
        obra_id = str(obra.id)
        if obra_id not in self.cart:
            self.cart[obra_id] = {'cantidad': 0, 'precio': str(obra.Precio)}
        self.cart[obra_id]['cantidad'] += cantidad
        self.guardar()

    def guardar(self):
        self.session.modified = True

    def eliminar(self, obra_id):
        obra_id = int(obra_id)
        str_obra_id = str(obra_id)
        if str_obra_id in self.cart:
            del self.cart[str_obra_id]
            self.guardar()


    def get_obras(self):
        obra_ids = self.cart.keys()
        obras = Obras.objects.filter(id__in=obra_ids)
        cart = self.cart.copy()
        for obra in obras:
            obra_id = str(obra.id)
            cart[obra_id]['obra'] = obra
            cart[obra_id]['cantidad'] = cart[obra_id]['cantidad']
            cart[obra_id]['total_precio'] = Decimal(obra.Precio) * cart[obra_id]['cantidad']
            cart[obra_id]['nombre'] = obra.Nombre
            cart[obra_id]['imagen'] = obra.image.url
        return cart.values()



    def get_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.cart.values())

    def limpiar(self):
        del self.session[settings.CART_SESSION_ID]
        self.guardar()

    def actualizar_cantidad(self, obra_id, cantidad):
        obra_id = str(obra_id)
        if obra_id in self.cart:
            self.cart[obra_id]['cantidad'] = cantidad
            self.guardar()