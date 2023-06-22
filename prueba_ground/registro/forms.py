from django import forms
from .models import UsersRegistro

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UsersRegistro
        fields = '__all__'