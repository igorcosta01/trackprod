from django.shortcuts import render
from .models import ProdutoAcabado
# from .forms import formProdutoAcabado
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.


def list_produto_acabado(request):
    produto_acabado = ProdutoAcabado.objects.order_by('data_entrada')

    context = {'produto_acabado': produto_acabado}
    return render(request, 'estoque_acabado/list-produto-acabado.html', context)

def produto_acabado(request, produto_acabado_id):
    produto_acabado = ProdutoAcabado.objects.get(id = produto_acabado_id)

    context = {'produto_acabado': produto_acabado}
    return render(request, 'estoque_acabado/produto_acabado.html', context)