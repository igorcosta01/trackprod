from django.shortcuts import render
from .forms import ProdutoForm, UnidadeMedidaForm
from .models import Produto

# Create your views here.

def produto(request, produto_id):
    produto = Produto.objects.get(id = produto_id)

    context = {'produto': produto}
    return render(request, 'produto/produto.html', context)

def novo_produto(request):
    """Página de cadastro de produto"""
    if request.method != 'POST':
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.save()
    
    context = {'form': form}
    return render(request, 'produto/novo_produto.html', context)

def list_produtos(request):
    list_produtos = Produto.objects.all()
    context = {'list_produtos': list_produtos}
    return render(request, 'produto/list_produtos.html', context)