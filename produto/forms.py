from django import forms
from .models import Produto

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','descricao', 'preco','image']