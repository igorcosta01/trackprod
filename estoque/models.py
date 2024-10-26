from django.db import models
from cadastro.models import UnidadeMedida, Produto
from producao.models import OrdemProducao

# Create your models here.

class ProdutoAcabado(models.Model):

    # ordem_producao = models.ForeignKey(OrdemProducao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=0)
    data_entrada = models.DateField(auto_now_add=True)
    localizacao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Produtos Acabados"

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

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

# class MovimentoEstoque(models.Model):
#     TIPO_MOVIMENTOS_CHOICES = [
#         ('entrada', 'Entrada'),
#         ('saida', 'Saída'),
#         ('ajuste', 'Ajuste'),
#     ]

#     material = models.ForeignKey(Material, on_delete=models.CASCADE)
#     quantidade_movimentada = models.DecimalField(max_digits=10, decimal_places=2)
#     unidade_medida = models.CharField()