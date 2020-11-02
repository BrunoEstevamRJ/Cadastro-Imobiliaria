from django import forms
from .models import Clientes


class ProductForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['cliente', 'telefone', 'email']
