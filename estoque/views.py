from django.shortcuts import render
from .models import ProdutoAcabado, MovimentoEstoqueAcabado, Funcionario, Produto, OrdemProducao, Drive
from .forms import ProdutoAcabadoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.

@login_required
def list_produto_acabado(request,):
    produto_acabado = ProdutoAcabado.objects.order_by('data_entrada')

    context = {'produto_acabado': produto_acabado}
    return render(request, 'estoque_acabado/list-produto-acabado.html', context)

@login_required
def produto_acabado(request, produto_acabado_id):
    produto_acabado = ProdutoAcabado.objects.get(id = produto_acabado_id)

    movimentacoes = MovimentoEstoqueAcabado.objects.filter(produto_acabado=produto_acabado)

    context = {'movimentacoes': movimentacoes, 'produto_acabado': produto_acabado}
    return render(request, 'estoque_acabado/produto_acabado.html', context)

@login_required
def novo_produto_acabado(request):
    if request.method == 'POST':
        produto_codigo = request.POST.get('codigo_produto')
        qtdEntrada = request.POST.get('qtdEntrada')
        localizacao = request.POST.get('drive_id')
        peso_liq_caixa = request.POST.get('peso_liq_caixa')
        peso_brt_caixa = request.POST.get('peso_brt_caixa')
        cartucho = request.POST.get('cartucho')
        qtd_total_caixa = request.POST.get('qtd_total_caixa')

        produto = get_object_or_404(Produto, codigo=produto_codigo)

        ProdutoAcabado.objects.create(
            produto=produto,
            quantidade=qtdEntrada,
            localizacao=localizacao,
            peso_liq_caixa=peso_liq_caixa,
            peso_brt_caixa=peso_brt_caixa,
            cartucho=cartucho,
            qtd_total_caixa=qtd_total_caixa
        )

        return HttpResponseRedirect(reverse('estoque_acabado/list-produto-acabado.html'))
    
    # Se o método não for POST, renderiza o formulário.
    return render(request, 'estoque_acabado/novo_produto_acabado.html')

@login_required
def mov_estoque_acabado(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        tipo_movimento = request.POST.get('tipo_movimento')
        quantidade = int(request.POST.get('quantidade'))
        data_mov = request.POST.get('data_mov')
        endereco = request.POST.get('endereco')
        matricula_funcionario = request.POST.get('funcionario')

        # Obtém o ProdutoAcabado correspondente
        produto_acabado = get_object_or_404(ProdutoAcabado, id=produto_id)

        funcionario = get_object_or_404(Funcionario, matricula_funcionario=matricula_funcionario)

        # Cria uma nova movimentação de estoque
        nova_movimentacao = MovimentoEstoqueAcabado.objects.create(
            produto_acabado=produto_acabado,
            tipo_movimento=tipo_movimento,
            quantidade_movimentada=quantidade,
            funcionario=funcionario,
            data_mov=data_mov,
            endereco=endereco,
        )

        # Redireciona para uma página de sucesso ou detalhe do produto acabado
        return HttpResponseRedirect(reverse('produto_acabado', args=[produto_acabado.id]))
    
@login_required
def ordens_producao_entrada_estoque(request):
    ordens_producao = OrdemProducao.objects.filter(status="finalizada").order_by('data_criacao')
    context = {'ordens_producao': ordens_producao}
    return render(request, 'estoque_acabado/ordens_producao_finalizadas.html', context)

def entrada_estoque(request, ordem_producao_id):
    drives = Drive.objects.order_by('rua', 'numero')
    ordem_producao = get_object_or_404(OrdemProducao, id=ordem_producao_id)
    
    if request.method == 'POST':
        produto_codigo = request.POST.get('codigo_produto')
        qtdEntrada = request.POST.get('qtdEntrada')
        localizacao_id = request.POST.get('drive_id')
        peso_liq_caixa = request.POST.get('peso_liq_caixa')
        peso_brt_caixa = request.POST.get('peso_brt_caixa')
        cartucho = request.POST.get('cartucho')
        qtd_total_caixa = request.POST.get('qtd_total_caixa')

        produto = get_object_or_404(Produto, codigo=produto_codigo)
        drive = get_object_or_404(Drive, id=localizacao_id, ocupado=False)


        ProdutoAcabado.objects.create(
            produto=produto,
            quantidade=qtdEntrada,
            localizacao=f"{drive.rua}{drive.numero}",	
            peso_liq_caixa=peso_liq_caixa,
            peso_brt_caixa=peso_brt_caixa,
            cartucho=cartucho,
            qtd_total_caixa=qtd_total_caixa
        )

        drive.ocupado = True
        drive.produto = produto
        drive.save()

        return HttpResponseRedirect(reverse('estoque_acabado:list-produto-acabado'))

    return render(request, 'estoque_acabado/entrada_estoque.html', {'drives': drives, 'ordem_producao': ordem_producao})