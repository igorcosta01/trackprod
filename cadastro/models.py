from django.db import models

# Create your models here.

class Cliente(models.Model):

    TIPOS_CLIENTE = [
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica'),
    ]
 
    nome_cliente = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=2, choices=TIPOS_CLIENTE, default='pf')
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_cliente


######################## PRODUTO #################################
class Produto(models.Model):

    TIPO_PRODUTO = [
        ('TAMPA', 'Tampa'),
        ('COPO', 'Copo'),
        ('POTE', 'Pote'),
        ('BANDEJA', 'Bandeja'),
        ('PRATO', 'Prato'),
        ('KIT POTE', 'Kit Pote'),
    ]

    STATUS_PRODUTO = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_PRODUTO, null=True)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)
    material = models.CharField(max_length=100, null=True, blank=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    volume = models.IntegerField(null=True)
    cor = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=7, choices=STATUS_PRODUTO, default="ativo", null=True)

    def __str__(self):
        return self.codigo
    
class UnidadeMedida(models.Model):
    unidade_medida = models.CharField(max_length=50)
    abreviacao = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.unidade_medida} - {self.abreviacao}"


#################### FUNCIONARIO ####################################
class Funcionario(models.Model):

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),        ('inativo', 'Inativo'),
    ]

    nome_funcionario = models.CharField(max_length=100)
    matricula_funcionario = models.CharField(max_length=5, unique=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="ativo")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_funcionario