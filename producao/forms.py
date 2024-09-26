from django import forms
from .models import OrdemProducao, Maquina

class OrdemProducaoForm(forms.ModelForm):
    class Meta:
        model = OrdemProducao
        previsao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # Adiciona o widget correto
        )
        fields = ['produto', 'quantidade', 'data_previsao', 'status']
        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',
            'data_previsao': 'Previsão',
            'status': 'Status',
        }

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['nome', 'codigo', 'observacao', 'capacidade_producao']
        labels = {
            'nome': 'Maquina', 
            'codigo': 'Código', 
            'observacao': 'Observação', 
            'capacidade_producao': 'Capacidade Produtiva (Dia)'
            }