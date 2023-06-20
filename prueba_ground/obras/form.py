from django import forms
from .models import Obras

class CreateObraForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = '__all__'