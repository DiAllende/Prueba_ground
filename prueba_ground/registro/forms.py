from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = f"user_{CustomUser.objects.count() + 1}"  # Genera un username único
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        return email
    
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
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
