from django import forms
from cadastro.models import Produto, UnidadeMedida, Funcionario

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control form-control'}),  # Estilizando o select
            'tipo': forms.Select(attrs={'class': 'form-control form-control'}),  # Estilizando o select
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control'}),  # Estilizando o select
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição do Produto'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Peso', 'min': '0'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Volume', 'min': '0'}),
            'cor': forms.TextInput(attrs={'class': 'form-control form-control'}),
        }

        fields = ['cliente', 'tipo', 'codigo', 'descricao', 'material', 'peso', 'volume', 'cor']
        labels = {
            'cliente': 'Cliente',
            'tipo': 'Tipo',
            'codigo': 'Código (SKU)',
            'descricao': 'Descrição',
            'material': 'Material',
            'peso': 'Peso (g)',
            'volume': 'Volume (ml)',
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

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'matricula_funcionario', 'status',]
        labels = {
            'nome_funcionario': 'Nome',
            'matricula_funcionario': 'Matrícula',
            'status': 'Status',
        }