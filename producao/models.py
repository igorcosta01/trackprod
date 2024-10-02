from django.db import models
from cadastro.models import Produto, Funcionario, Cliente
from django.utils import timezone

# Create your models here.

# class OrdemProducao(models.Model):
#     STATUS_CHOICES = [
#         ('pendente', 'Pendente'),
#         ('em_producao', 'Em Produção'),
#         ('finalizada', 'Finalizada'),
#     ]

#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     quantidade = models.IntegerField()
#     data_criacao = models.DateTimeField(auto_now_add=True)
#     data_previsao = models.DateField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

#     class Meta:
#         verbose_name_plural = 'ordens_de_producao'

#     def __str__(self):
#         return self.id
    
class OrdemProducao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('finalizado', 'Finalizado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    quantidade_apontada = models.IntegerField(default=0)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pendente')
    data_previsao = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ordens_de_producao'

    def __str__(self):
        return f"Ordem de Produção {self.id} - {self.produto.nome}"

    # Inicia a produção
    def iniciar_producao(self):
        self.status = 'em_andamento'
        self.save()

    # Atualiza a quantidade apontada e o status
    def atualizar_quantidade_apontada(self, quantidade):
        self.quantidade_apontada += quantidade
        self.atualizar_status()
        self.save()

    # Regras de negócio para o status
    def atualizar_status(self):
        if self.quantidade_apontada >= self.quantidade_solicitada:
            self.status = 'finalizado'
        elif self.quantidade_apontada > 0:
            self.status = 'em_andamento'
        else:
            self.status = 'pendente'
            


########################### MAQUINAS ################################
    
class Maquina(models.Model):

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
        
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    observacao = models.CharField(max_length=300, blank=True, null=True)
    capacidade_producao = models.DecimalField(max_digits=10, decimal_places=2)
    em_manutencao = models.BooleanField(default=False)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="ativo")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# class ApontamentoProducao(models.Model):
#     ordem_producao = models.ForeignKey(OrdemProducao, on_delete=models.CASCADE)
#     quantidade_produzida = models.IntegerField()
#     maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
#     funcionario_apontamento = models.ForeignKey(Funcionario, on_delete=models.CASCADE, default=1)
#     inicio_producao = models.DateTimeField()
#     fim_producao = models.DateTimeField()
#     data_input_apontamento = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Apontamentos'

#     def __str__(self):
#         return f"Apontamento OP {self.ordem_producao.id} - {self.maquina.nome_maquina}"
    
class ApontamentoProducao(models.Model):
    ordem_producao = models.ForeignKey(OrdemProducao, on_delete=models.CASCADE)
    quantidade_produzida = models.IntegerField(null=True, blank=True)  # Quantidade apenas no fechamento
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    funcionario_apontamento = models.ForeignKey(Funcionario, on_delete=models.CASCADE, default=1)
    inicio_producao = models.DateTimeField()  # Registrado no início
    fim_producao = models.DateTimeField(null=True, blank=True)  # Definido no fechamento
    data_input_apontamento = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Apontamentos'

    def __str__(self):
        return f"Apontamento OP {self.ordem_producao.id} - {self.maquina.nome}"

    # Lógica de finalização de produção
    def fechar_producao(self, quantidade_produzida):
        self.quantidade_produzida = quantidade_produzida
        self.fim_producao = timezone.now()  # Define o tempo de fechamento
        self.save()

        # Atualiza a ordem de produção
        self.ordem_producao.atualizar_quantidade_apontada(quantidade_produzida)
