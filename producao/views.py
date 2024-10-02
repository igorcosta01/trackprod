from django.shortcuts import get_object_or_404, render
from .models import OrdemProducao, ApontamentoProducao, Maquina
from cadastro.models import Funcionario
from .forms import OrdemProducaoForm, MaquinaForm, EditMaquinaForm, IniciarProducaoForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
    return render(request, 'producao/iniciar_apontamento.html', context)

def iniciar_producao(request):
    if request.method != 'POST':
        form = IniciarProducaoForm()
    else:
        form = IniciarProducaoForm(request.POST)
        if form.is_valid():
            iniciar_producao = form.save(commit=False)

            ordem_producao = get_object_or_404(OrdemProducao)
            ordem_producao.status = 'Em andamento'

            iniciar_producao.save()

            return HttpResponseRedirect(reverse('ordem_producao', args=[ordem_de_producao.id]))

    context = {'form': form}
    return render(request, 'producao/iniciar_apontamento.html', context)

# def iniciar_producao(request, ordem_producao_id):
#     if request.method != 'POST':
#         form = IniciarProducaoForm(id = ordem_producao_id)
#     else:
#         form = IniciarProducaoForm(request.POST)
#         if form.is_valid():
#             matricula_funcionario = form.cleaned_data['matricula_funcionario']
#             ordem_producao_id = form.cleaned_data['ordem_producao']

#             # Valida o funcionário
#             funcionario = get_object_or_404(Funcionario, matricula_funcionario=matricula_funcionario)

#             # Valida a ordem de produção
#             ordem_producao = get_object_or_404(OrdemProducao, id=ordem_producao_id)

#             # Atualiza a ordem de produção para "Em andamento"
#             ordem_producao.status = 'Em andamento'
#             ordem_producao.save()

#             # Inicia a produção (cria um apontamento)
#             ApontamentoProducao.objects.create(
#                 ordem_producao=ordem_producao,
#                 funcionario_apontamento=funcionario,
#                 maquina=ordem_producao.maquina,  # Supondo que a ordem tenha uma máquina associada
#                 inicio_producao=form.cleaned_data['inicio_producao']
#             )

#             return HttpResponseRedirect(reverse('sucesso_inicio_producao'))

#     context = {'form': form}
#     return render(request, 'producao/iniciar_producao.html', context)


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