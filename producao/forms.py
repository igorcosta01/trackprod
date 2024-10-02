from django import forms
from .models import OrdemProducao, Maquina, ApontamentoProducao

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
        

class IniciarProducaoForm(forms.ModelForm):
    class Meta:
        model = ApontamentoProducao
        fields = ['ordem_producao', 'maquina', 'funcionario_apontamento', 'quantidade_produzida', 'inicio_producao']
        labels = {
            'ordem_producao': 'Ordem de Produção',
            'maquina': 'Máquina',
            'funcionario_apontamento': 'Funcionário (Número de Cadastro)',
            'quantidade_produzida': 'Quantidade Produzida',
            'inicio_producao': 'Início da Produção',
        }
