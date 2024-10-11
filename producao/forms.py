from django import forms
from .models import OrdemProducao, Maquina, ApontamentoProducao

class OrdemProducaoForm(forms.ModelForm):
    class Meta:
        model = OrdemProducao
        previsao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # Adiciona o widget correto
        )
        fields = ['cliente', 'produto', 'quantidade', 'data_previsao']
        labels = {
            'cliente': 'Cliente',
            'produto': 'Produto',
            'quantidade': 'Quantidade',
            'data_previsao': 'Previsão',
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

class EditMaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['nome', 'codigo', 'observacao', 'capacidade_producao', 'status']
        labels = {
            'nome': 'Maquina', 
            'codigo': 'Código', 
            'observacao': 'Observação', 
            'capacidade_producao': 'Capacidade Produtiva (Dia)',
            'status': 'Status', 
            }
        
class ApontamentoProducaoForm(forms.ModelForm):
    class Meta:
        model = ApontamentoProducao
        fields = ['funcionario_apontamento', 'maquina', 'inicio_producao', 'quantidade_produzida', 'fim_producao']

        widgets = {
            'inicio_producao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Input para data e hora
            'fim_producao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),     # Input para data e hora
            'quantidade_produzida': forms.NumberInput(attrs={'min': '0'}),            # Input para números
        }

        labels = {
            'funcionario': 'Funcionário',
            'maquina': 'Máquina',
            'inicio_producao': 'Iniciado em:',
            'quantidade_produzida': 'Quantidade Produzida',
            'fim_producao': 'Finalizado em:',
        }