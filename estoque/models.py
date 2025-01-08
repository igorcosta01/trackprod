from django.db import models, transaction
from cadastro.models import UnidadeMedida, Produto, Funcionario
from producao.models import OrdemProducao

# Create your models here.

class Drive(models.Model):
    rua = models.CharField(max_length=1, choices=[('A', 'Rua A'), ('B', 'Rua B'), ('C', 'Rua C')])
    numero = models.PositiveIntegerField()
    ocupado = models.BooleanField(default=False)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('rua', 'numero')

    def __str__(self):
        return f"{self.rua}{self.numero}"

class ProdutoAcabado(models.Model):

    # ordem_producao = models.ForeignKey(OrdemProducao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=0)
    data_entrada = models.DateField(auto_now_add=True)
    localizacao = models.CharField(max_length=5, null=True)
    peso_liq_caixa = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    peso_brt_caixa = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    cartucho = models.CharField(max_length=8)
    qtd_total_caixa = models.IntegerField(default=0, null=True)
    codigo_barra = models.CharField(max_length=13, blank=True, null=True)
    codigo_barra_pct = models.CharField(max_length=13, blank=True, null=True)
    lote = models.CharField(max_length=10, null=True)
    data_fabricacao = models.DateField(null=True)

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
    endereco = models.CharField(max_length=5, null=True)

    class Meta:
        verbose_name_plural = "Movimentações PA"

    def save(self, *args, **kwargs):
        if not self.pk:  # Apenas na criação
            with transaction.atomic():
                # Atualiza a quantidade do ProdutoAcabado
                if self.tipo_movimento == 'entrada':
                    self.produto_acabado.quantidade += self.quantidade_movimentada
                elif self.tipo_movimento == 'saida':
                    self.produto_acabado.quantidade -= self.quantidade_movimentada

                # Atualiza a localização
                self.produto_acabado.localizacao = self.endereco
                self.produto_acabado.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto_acabado.produto.codigo} ({self.quantidade_movimentada})pcs"


