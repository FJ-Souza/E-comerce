from django import forms
from django.forms import ModelForm
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = "__all__"
        labels = {
            "name": "produto",
            "description": "descricao",
            "price": "Valor",
            "path": "img",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'produto',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'descricao',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '10,00',
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'placeholder': 'img',
                }
            ),
        }