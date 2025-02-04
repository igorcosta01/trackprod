import django_filters
from .models import ProdutoAcabado
from django import forms

class FilterProdutoAcabado(django_filters.FilterSet):
    produto = django_filters.CharFilter(
        field_name="produto__codigo",  # Substitua pelo campo correto
        lookup_expr="icontains",
        label="Produto",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    
    localizacao = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Endereço",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = ProdutoAcabado
        fields = ["produto", "localizacao"]


# class FilterProdutoAcabado(django_filters.FilterSet):
#     class Meta:
#         model = ProdutoAcabado
#         fields = {
#             'produto__codigo': ['icontains'],
#             'localizacao': ['icontains'],
#         }