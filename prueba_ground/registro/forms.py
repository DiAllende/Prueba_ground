from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.generate_unique_username(user.nombre)
        if commit:
            user.save()
        return user

    def generate_unique_username(self, nombre):
        base_username = nombre.lower().replace(' ', '_')
        username = base_username
        count = 1
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}_{count}"
            count += 1
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está registrado.")
        return cleaned_data

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'nombre', 'rut', 'direccion', 'pais', 'cp', 'admin')

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'rut', 'direccion', 'pais', 'admin']

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control field-spacing', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control field-spacing', 'placeholder': 'Contraseña'})
    )