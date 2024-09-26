from django.db import models
from cadastro.models import Produto, Funcionario
# Create your models here.

class OrdemProducao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_producao', 'Em Produção'),
        ('finalizada', 'Finalizada'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_previsao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name_plural = 'ordens_de_producao'

    def __str__(self):
        return self.id
    
class Maquina(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    observacao = models.CharField(max_length=300, blank=True, null=True)
    capacidade_producao = models.DecimalField(max_digits=10, decimal_places=2)
    em_manutencao = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class ApontamentoProducao(models.Model):
    ordem_producao = models.ForeignKey(OrdemProducao, on_delete=models.CASCADE)
    quantidade_produzida = models.IntegerField()
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    funcionario_apontamento = models.ForeignKey(Funcionario, on_delete=models.CASCADE, default=1)
    inicio_producao = models.DateTimeField()
    fim_producao = models.DateTimeField()
    data_input_apontamento = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Apontamentos'

    def __str__(self):
        return f"Apontamento OP {self.ordem_producao.id} - {self.maquina.nome_maquina}"
    