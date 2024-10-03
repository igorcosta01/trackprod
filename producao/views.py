from django.shortcuts import render
from .models import OrdemProducao, ApontamentoProducao, Maquina
from .forms import OrdemProducaoForm, MaquinaForm, EditMaquinaForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """Index da aplicação"""
    return render(request, 'index.html')



def ordem_de_producao(request, ordem_producao_id):
    ordem_producao = OrdemProducao.objects.get(id = ordem_producao_id)

    context = {'ordem_producao': ordem_producao}
    return render(request, 'producao/ordem_producao.html', context)

def list_ordem_producao(request):
    ordens_producao = OrdemProducao.objects.order_by('data_criacao')
    context = {'ordens_producao' : ordens_producao}
    return render(request, 'producao/list-ordem-producao.html', context)

def nova_ordem_producao(request):
    if request.method != 'POST':
        form = OrdemProducaoForm()
    else:
        form = OrdemProducaoForm(request.POST)
        if form.is_valid():
            nova_ordem_producao = form.save(commit=False)
            nova_ordem_producao.save()
            return HttpResponseRedirect(reverse('list_ordens'))

    context = {'form': form}
    return render(request, 'producao/new_ordem_producao.html', context)


############################################  MAQUINAS  ############################################

def maquina(request, maquina_id):
    maquina = Maquina.objects.get(id = maquina_id)

    context = {'maquina': maquina}
    return render(request, 'maquina/maquina.html', context)

def nova_maquina(request):
    if request.method != 'POST':
        form = MaquinaForm()
    else:
        form = MaquinaForm(request.POST)
        if form.is_valid():
            nova_maquina = form.save(commit=False)
            nova_maquina.save()
            return HttpResponseRedirect(reverse('list_maquinas'))
    
    context = {'form': form}
    return render(request, 'maquina/nova_maquina.html', context)

def list_maquinas(request):
    maquinas = Maquina.objects.all()
    context = {'maquinas': maquinas}
    return render(request, 'maquina/list_maquinas.html', context)

def edit_maquina(request, maquina_id):
    """Edita um entrada já cadastrada"""
    maquina = Maquina.objects.get(id=maquina_id)

    #Garante que o assunto pertence ao usuário atual
    # if topic.owner != request.user:
    #     raise Http404

    if request.method != 'POST':
        form = EditMaquinaForm(instance=maquina)
    else:
        # Dados de POST submetidos processa os dados
        form = EditMaquinaForm(instance=maquina, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('maquina', args=[maquina.id]))
    
    context = {'maquina': maquina, 'form': form}
    return render(request, 'maquina/edit_maquina.html', context)