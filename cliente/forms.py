from django import forms
from .models import Cliente


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','endereco', 'telefone', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }