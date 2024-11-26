from django import forms
from .models import ProdutoAcabado

class ProdutoAcabadoForm(forms.ModelForm):
    class Meta:
        model = ProdutoAcabado
        fields = ['produto', 'quantidade', 'localizacao', 'peso_liq_caixa', 'peso_brt_caixa', 'cartucho', 'qtd_total_caixa']

        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control form-control-sm'}),  # Estilizando o select
            'quantidade': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),  # Estilizando o select
            'localizacao': forms.TextInput(attrs={'type': 'text', 'class': 'form-control form-control-sm'}),  # Input de data e hora
            'peso_liq_caixa': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'peso_brt_caixa': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'cartucho': forms.TextInput(attrs={'type': 'text', 'class': 'form-control form-control-sm'}),
            'qtd_total_caixa': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }

        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',
            'localizacao': 'Endereço',
            'peso_liq_caixa': 'Peso Liquido Caixa',
            'peso_brt_caixa': 'Peso Bruto Caixa',
            'cartucho': 'Cartucho',
            'qtd_total_caixa': 'Quantidade Total Caixa',
        }