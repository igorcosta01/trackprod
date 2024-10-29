from django import forms
from .models import ProdutoAcabado

class ProdutoAcabadoForm(forms.ModelForm):
    class Meta:
        model = ProdutoAcabado
        fields = ['produto', 'quantidade', 'localizacao']

        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control form-control-sm'}),  # Estilizando o select
            'quantidade': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),  # Estilizando o select
            'localizacao': forms.TextInput(attrs={'type': 'text', 'class': 'form-control form-control-sm'}),  # Input de data e hora
        }

        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',
            'localizacao': 'Endereço',
        }