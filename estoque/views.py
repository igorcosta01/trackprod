from django.shortcuts import render
from .models import ProdutoAcabado
# from .forms import formProdutoAcabado
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def list_produto_acabado(request):
    produto_acabado = ProdutoAcabado.objects.order_by('data_entrada')
    context = {'produto_acabado': produto_acabado}
    return render(request, 'list-produto-acabado.html', context)