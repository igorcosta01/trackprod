from django.shortcuts import render, get_object_or_404
from .models import OrdemProducao, Maquina, ApontamentoProducao, Produto
from .forms import OrdemProducaoForm, MaquinaForm, EditMaquinaForm, ApontamentoProducaoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    """Index da aplicação"""
    return render(request, 'index.html')



def ordem_de_producao(request, ordem_producao_id):
    # Obter a ordem de produção
    ordem_producao = OrdemProducao.objects.get(id=ordem_producao_id)
    
    # Obter os apontamentos relacionados à ordem de produção
    apontamentos = ApontamentoProducao.objects.filter(ordem_producao=ordem_producao)
    
    context = {'ordem_producao': ordem_producao, 'apontamentos': apontamentos}
    return render(request, 'producao/ordem_producao.html', context)

def list_ordem_producao(request):
    ordens_producao = OrdemProducao.objects.order_by('data_criacao')
    context = {'ordens_producao': ordens_producao}
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

def nova_ordem_producao_modal(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = request.POST.get('quantidade')
        data_previsao = request.POST.get('data_previsao')

        # Obtém o produto e o cliente associado ao produto
        produto = get_object_or_404(Produto, id=produto_id)
        cliente = produto.cliente  # Supondo que o cliente esteja associado ao produto

        # Cria uma nova Ordem de Produção com as informações fornecidas
        nova_ordem = OrdemProducao.objects.create(
            cliente=cliente,
            produto=produto,
            quantidade=quantidade,
            data_previsao=data_previsao
        )

        # Redireciona para a lista de ordens de produção ou página de sucesso
        return HttpResponseRedirect(reverse('produto' , args=[produto.id]))



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


####################### Apontamento ##################################

def apontar_ordem_producao(request, ordem_producao_id):
    ordem_producao = get_object_or_404(OrdemProducao, id=ordem_producao_id)
    op_finalizada = False
    mostrar_alerta = False  # Controle para exibir o alerta apenas após o POST

    if request.method == 'POST':
        form = ApontamentoProducaoForm(request.POST)
        if ordem_producao.status == 'finalizada':
            op_finalizada = True
            mostrar_alerta = True  # Exibe o alerta somente após tentar salvar
        elif form.is_valid():
            apontamento = form.save(commit=False)
            apontamento.ordem_producao = ordem_producao
            apontamento.inicio_producao = timezone.now()
            apontamento.save()
            return HttpResponseRedirect(reverse('list_ordens'))
    else:
        form = ApontamentoProducaoForm()

    context = {
        'form': form,
        'ordem_producao': ordem_producao,
        'mostrar_alerta': mostrar_alerta  # Passa a flag para o template
    }
    return render(request, 'producao/apontamento_form.html', context)

