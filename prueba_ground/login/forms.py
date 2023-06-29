from django import forms
from .models import UsersRegistro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = UsersRegistro
        fields = ['email', 'password']

