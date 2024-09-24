from django import forms
from cadastro.models import Produto, UnidadeMedida, Material, Maquina

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'descricao', 'material', 'peso', 'volume', 'cor']
        labels = {
            'nome': 'Nome',
            'codigo': 'Código',
            'descricao': 'Descrição',
            'material': 'Material',
            'peso': 'Peso',
            'volume': 'Volume',
            'cor': 'Cor'
        }

class UnidadeMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadeMedida
        fields = ['unidade_medida', 'abreviacao']
        labels = {
            'unidade_medida': 'Nome UM',
            'abreviacao': 'Abreviação'
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