from django import forms
from .models import UsersRegistro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = UsersRegistro
        fields = ['email', 'password']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control field-spacing', }),
            'password': forms.TextInput(attrs={'class': 'form-control field-spacing'}),
        }

