from django import forms
from .models import UsersRegistro

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UsersRegistro
        fields = '__all__'
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control field-spacing', }),
            'password': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'rut': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'pais': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
            'cp': forms.TextInput(attrs={'class': 'form-control field-spacing'}),

        }