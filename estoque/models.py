from django.db import models
from cadastro.models import UnidadeMedida, Produto, Funcionario
from producao.models import OrdemProducao

# Create your models here.

class ProdutoAcabado(models.Model):

    # ordem_producao = models.ForeignKey(OrdemProducao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=0)
    data_entrada = models.DateField(auto_now_add=True)
    localizacao = models.CharField(max_length=20)

    peso_liq_caixa = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    peso_brt_caixa = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cartucho = models.CharField(max_length=8)
    qtd_total_caixa = models.IntegerField(default=0, null=True)
    codigo_barra = models.CharField(max_length=13, blank=True, null=True)
    codigo_barra_pct = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Produtos Acabados"

    def __str__(self):
        return f"{self.produto.codigo} - {self.quantidade}pcs"

class Material(models.Model):
    TIPO_CHOICES = [
        ('materia_prima', 'Matéria-Prima'),
        ('insumo', 'Insumo'),
        ('embalagem', 'Embalagem'),
    ]

    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=4, unique=True)
    descricao = models.TextField(blank=True)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=3)
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=3)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class MovimentoEstoqueAcabado(models.Model):
    TIPO_MOVIMENTOS_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto_acabado = models.ForeignKey(ProdutoAcabado, on_delete=models.CASCADE)
    tipo_movimento = models.CharField(max_length=10, choices=TIPO_MOVIMENTOS_CHOICES)
    quantidade_movimentada = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_mov = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Movimentações PA"

    def save(self, *args, **kwargs):
        # Atualiza o saldo na model ProdutoAcabado
        if self.tipo_movimento == 'entrada':
            self.produto_acabado.quantidade += self.quantidade_movimentada
        elif self.tipo_movimento == 'saida':
            self.produto_acabado.quantidade -= self.quantidade_movimentada

        self.produto_acabado.localizacao = self.endereco
        
        self.produto_acabado.save()  # Salva a atualização no saldo do produto
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto_acabado.produto.codigo} ({self.quantidade_movimentada})pcs"