from django import forms
from .models import Users

class FormLog(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput)

