from django.shortcuts import render
from .forms import ProdutoForm, UnidadeMedidaForm, FuncionarioForm
from .models import Produto, Funcionario
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

################ PRODUTOS ###################
@login_required
def produto(request, produto_id):
    produto = Produto.objects.get(id = produto_id)

    context = {'produto': produto}
    return render(request, 'produto/produto.html', context)

@login_required
def novo_produto(request):
    """Página de cadastro de produto"""
    if request.method != 'POST':
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.save()
            return HttpResponseRedirect(reverse('list_produtos'))
    
    context = {'form': form}
    return render(request, 'produto/novo_produto.html', context)
    
@login_required
def list_produtos(request):
    list_produtos = Produto.objects.all()
    context = {'list_produtos': list_produtos}
    return render(request, 'produto/list_produtos.html', context)

####################### FUNCIONARIOS ###############################

@login_required
def list_funcionarios(request):
    list_funcionarios = Funcionario.objects.all()
    context = {'list_funcionarios': list_funcionarios}
    return render(request, 'funcionario/list_funcionarios.html', context)

@login_required
def novo_funcionario(request):
    """Página de cadastro de produto"""
    if request.method != 'POST':
        form = FuncionarioForm()
    else:
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            novo_funcionario = form.save(commit=False)
            novo_funcionario.save()
            messages.success(request, "Salvo com sucesso")
            return HttpResponseRedirect(reverse('list_funcionarios'))
    
    context = {'form': form}
    return render(request, 'funcionario/novo_funcionario.html', context)
