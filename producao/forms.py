from django import forms
from .models import OrdemProducao

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