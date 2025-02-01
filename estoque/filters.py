import django_filters
from .models import ProdutoAcabado

# class FilterProdutoAcabado(django_filters.FilterSet):
#     produto = django_filters.CharFilter(lookup_expr='icontains')
#     localizacao = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = ProdutoAcabado
#         fields = ['produto', 'localizacao']

class FilterProdutoAcabado(django_filters.FilterSet):
    class Meta:
        model = ProdutoAcabado
        fields = {
            'produto__codigo': ['icontains'],
            'localizacao': ['icontains'],
        }