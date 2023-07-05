from django import forms
from .models import Obras

class CreateObraForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = '__all__'

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Precio': forms.NumberInput(attrs={'class': 'form-control field-spacing'}),
            'Autor': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Titulo_Original': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Tecnica': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Anio': forms.NumberInput(attrs={'class': 'form-control field-spacing'}),
            'Detalles_obra': forms.Textarea(attrs={'class': 'form-control field-spacing'}),
            'estado': forms.TextInput(attrs={'class': 'form-control field-spacing', 'readonly': 'readonly'}),
        }

class UpdateObraForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ('Nombre', 'Precio', 'Autor', 'Titulo_Original', 'Tecnica', 'Anio', 'Detalles_obra', 'image') 

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control field-spacing', }),
            'Precio': forms.NumberInput(attrs={'class': 'form-control field-spacing'}),
            'Autor': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Titulo_Original': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Tecnica': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'Anio': forms.NumberInput(attrs={'class': 'form-control field-spacing'}),
            'Detalles_obra': forms.Textarea(attrs={'class': 'form-control field-spacing'}),

        }