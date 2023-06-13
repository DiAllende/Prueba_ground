from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Email",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Ingresa tu email'}
    ),min_length=4, max_length=100)
    password = forms.PasswordInput(label="Password", required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Ingrese su contraseña'}
    ),min_length=8, max_length=50)