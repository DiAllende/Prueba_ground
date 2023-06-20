from django import forms
from .models import Obras

class CreateObraForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = '__all__'

class UpdateObraForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ['Nombre', 'Precio', 'Detalles_obra', 'image']