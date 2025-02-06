from django.shortcuts import render
from .models import ProdutoAcabado, MovimentoEstoqueAcabado, Funcionario, Produto, OrdemProducao, Drive
from .filters import FilterProdutoAcabado
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import transaction

# Create your views here.

@login_required
def list_produto_acabado(request):
    produto_acabado = ProdutoAcabado.objects.order_by('data_entrada').filter(tipo="acabado")
    ultima_movimentacao = MovimentoEstoqueAcabado.objects.order_by('data_mov').last()

    filter_produto_acabado = FilterProdutoAcabado(request.GET, queryset=produto_acabado)

    context = {'produto_acabado': filter_produto_acabado.qs, 'ultima_movimentacao': ultima_movimentacao, 'filter_produto_acabado': filter_produto_acabado}
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
        qtdEntrada = request.POST.get('qtdSolicitada_display')
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
    ordens_producao = OrdemProducao.objects.filter(status="finalizada", is_estoque=False).order_by('data_criacao')
    context = {'ordens_producao': ordens_producao}
    return render(request, 'estoque_acabado/ordens_producao_finalizadas.html', context)

def entrada_estoque(request, ordem_producao_id):
    drives = Drive.objects.order_by('rua', 'numero')
    ordem_producao = get_object_or_404(OrdemProducao, id=ordem_producao_id)
    produtos = Produto.objects.all()

    if request.method == 'POST':
        produto_codigo = request.POST.get('codigo_produto')
        qtdEntrada = int(request.POST.get('qtdEntrada'))
        localizacao_id = request.POST.get('drive_id')
        matricula_funcionario = request.POST.get('matricula_funcionario')

        produto = get_object_or_404(Produto, codigo=produto_codigo)
        drive = get_object_or_404(Drive, id=localizacao_id, ocupado=False)

        # Busca o funcionário pela matrícula
        try:
            funcionario = Funcionario.objects.get(matricula_funcionario=matricula_funcionario)
        except Funcionario.DoesNotExist:
            messages.error(request, 'Funcionário não encontrado!')
            return redirect('entrada_estoque', ordem_producao_id=ordem_producao_id)

        try:
            with transaction.atomic():
                # Criação do ProdutoAcabado
                produto_acabado = ProdutoAcabado.objects.create(
                    produto=produto,
                    quantidade=0,  # Será atualizado pela movimentação
                    localizacao=f"{drive.rua}{drive.numero}",
                    lote = ordem_producao.lote,
                    data_fabricacao = ordem_producao.data_fabricacao
                )

                # Marca o drive como Ocupado
                drive.ocupado = True
                drive.produto = produto
                drive.save()

                # Adiciona um flag na OP que já foi dado entrada em estoque
                ordem_producao.is_estoque = True
                ordem_producao.save()

                # Criação da movimentação
                MovimentoEstoqueAcabado.objects.create(
                    produto_acabado=produto_acabado,
                    tipo_movimento='entrada',
                    quantidade_movimentada=qtdEntrada,
                    funcionario=funcionario,
                    endereco=f"{drive.rua}{drive.numero}"
                )

                messages.success(request, 'Entrada de estoque realizada com sucesso!')
                return redirect('list-produto-acabado')

        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {str(e)}")
            return redirect('entrada_estoque', ordem_producao_id=ordem_producao_id)

    return render(request, 'estoque_acabado/entrada_estoque_temp.html', {'drives': drives, 'ordem_producao': ordem_producao, 'produtos': produtos})

@login_required
def ordens_producao_entrada_estoque(request):
    ordens_producao = OrdemProducao.objects.filter(status="finalizada", is_estoque=False).order_by('data_criacao')
    context = {'ordens_producao': ordens_producao}
    return render(request, 'estoque_acabado/ordens_producao_finalizadas.html', context)

@login_required
def entrada_estoque_temp(request):
    ruas = Drive.objects.values_list('rua', flat=True).filter(tipo="acabado").distinct()
    drives = Drive.objects.order_by('rua', 'numero')
    # ordem_producao = get_object_or_404(OrdemProducao, id=ordem_producao_id)
    produtos = Produto.objects.all()
    endereco_sugerido = Drive.objects.filter(ocupado=False).first()

    if request.method == 'POST':
        produto_codigo = request.POST.get('produto_id')
        qtdEntrada = int(request.POST.get('qtdEntrada'))
        localizacao_id = request.POST.get('drive_id')
        matricula_funcionario = request.POST.get('matricula_funcionario')
        lote = request.POST.get('lote')
        data_fabricacao = request.POST.get('data_fabricacao')
        tipo = "acabado"

        produto = get_object_or_404(Produto, id=produto_codigo)
        drive = get_object_or_404(Drive, id=localizacao_id, ocupado=False)

        # Busca o funcionário pela matrícula
        try:
            funcionario = Funcionario.objects.get(matricula_funcionario=matricula_funcionario)
        except Funcionario.DoesNotExist:
            messages.error(request, 'Funcionário não encontrado!')
            # return redirect('entrada_estoque', ordem_producao_id=ordem_producao_id)

        try:
            with transaction.atomic():
                # Criação do ProdutoAcabado
                produto_acabado = ProdutoAcabado.objects.create(
                    produto=produto,
                    quantidade=0,  # Será atualizado pela movimentação
                    localizacao=f"{drive.rua}{drive.numero}",
                    lote = lote,
                    data_fabricacao = data_fabricacao,
                    tipo = tipo
                )

                # Marca o drive como Ocupado
                drive.ocupado = True
                drive.produto = produto
                drive.save()

                # # Adiciona um flag na OP que já foi dado entrada em estoque
                # ordem_producao.is_estoque = True
                # ordem_producao.save()

                # Criação da movimentação
                MovimentoEstoqueAcabado.objects.create(
                    produto_acabado=produto_acabado,
                    tipo_movimento='entrada',
                    quantidade_movimentada=qtdEntrada,
                    funcionario=funcionario,
                    endereco=f"{drive.rua}{drive.numero}"
                )

                messages.success(request, 'Entrada de estoque realizada com sucesso!')
                return redirect('list-produto-acabado')

        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {str(e)}")
            # return redirect('entrada_estoque', ordem_producao_id=ordem_producao_id)

    return render(request, 'estoque_acabado/entrada_estoque_temp.html', {'drives': drives, 'produtos': produtos, 'endereco_sugerido': endereco_sugerido, 'ruas': ruas})

def get_enderecos(request):
    rua = request.GET.get("rua")
    enderecos = Drive.objects.filter(rua=rua).values("id", "rua", "numero", "ocupado")
    return JsonResponse(list(enderecos), safe=False)




#####################################################################
#                                                                   #    
#                       ESTOQUE INTERMEDIARIO                       #
#                                                                   #
#####################################################################

@login_required
def list_estoque_intermediario(request):
    produto_armazenado = ProdutoAcabado.objects.order_by('data_entrada').filter(tipo="intermediario")
    ultima_movimentacao = MovimentoEstoqueAcabado.objects.order_by('data_mov').last()

    filter_produto_armazenado = FilterProdutoAcabado(request.GET, queryset=produto_armazenado)

    context = {'produto_armazenado': filter_produto_armazenado.qs, 'ultima_movimentacao': ultima_movimentacao, 'filter_produto_armazenado': filter_produto_armazenado}
    return render(request, 'estoque_acabado/estoque_intermediario/list_estoque_intermediario.html', context)

@login_required
def ordens_producao_entrada_estoque(request):
    ordens_producao = OrdemProducao.objects.filter(status="finalizada", is_estoque=False).order_by('data_criacao')
    context = {'ordens_producao': ordens_producao}
    return render(request, 'estoque_acabado/ordens_producao_finalizadas.html', context)

def entrada_estoque_intermediario(request):
    ruas = Drive.objects.values_list('rua', flat=True).filter(tipo="intermediario").distinct()
    drives = Drive.objects.order_by('rua', 'numero')
    # ordem_producao = get_object_or_404(OrdemProducao, id=ordem_producao_id)
    produtos = Produto.objects.all()
    endereco_sugerido = Drive.objects.filter(ocupado=False).filter(tipo="intermediario").first()

    if request.method == 'POST':
        produto_codigo = request.POST.get('produto_id')
        qtdEntrada = int(request.POST.get('qtdEntrada'))
        localizacao_id = request.POST.get('drive_id')
        matricula_funcionario = request.POST.get('matricula_funcionario')
        lote = request.POST.get('lote')
        data_fabricacao = request.POST.get('data_fabricacao')
        tipo = "intermediario"

        produto = get_object_or_404(Produto, id=produto_codigo)
        drive = get_object_or_404(Drive, id=localizacao_id, ocupado=False)

        # Busca o funcionário pela matrícula
        try:
            funcionario = Funcionario.objects.get(matricula_funcionario=matricula_funcionario)
        except Funcionario.DoesNotExist:
            messages.error(request, 'Funcionário não encontrado!')

        try:
            with transaction.atomic():
                # Criação do ProdutoAcabado
                produto_acabado = ProdutoAcabado.objects.create(
                    produto=produto,
                    quantidade=0,  # Será atualizado pela movimentação
                    localizacao=f"{drive.rua}{drive.numero}",
                    lote = lote,
                    data_fabricacao = data_fabricacao,
                    tipo = tipo
                )

                # Marca o drive como Ocupado
                drive.ocupado = True
                drive.produto = produto
                drive.save()

                # Criação da movimentação
                MovimentoEstoqueAcabado.objects.create(
                    produto_acabado=produto_acabado,
                    tipo_movimento='entrada',
                    quantidade_movimentada=qtdEntrada,
                    funcionario=funcionario,
                    endereco=f"{drive.rua}{drive.numero}"
                )

                messages.success(request, 'Entrada de estoque realizada com sucesso!')
                return redirect('list_estoque_intermediario')

        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {str(e)}")
            # return redirect('entrada_estoque', ordem_producao_id=ordem_producao_id)

    return render(request, 'estoque_acabado/estoque_intermediario/entrada_estoque_inter.html', {'drives': drives, 'produtos': produtos, 'endereco_sugerido': endereco_sugerido, 'ruas': ruas})

@login_required
def produto_intermediario(request, produto_intermediario_id):
    produto_intermediario = ProdutoAcabado.objects.get(id = produto_intermediario_id)

    movimentacoes = MovimentoEstoqueAcabado.objects.filter(produto_acabado=produto_intermediario)

    context = {'movimentacoes': movimentacoes, 'produto_intermediario': produto_intermediario}
    return render(request, 'estoque_acabado/estoque_intermediario/produto_intermediario.html', context)