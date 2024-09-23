from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    material = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo
    
class UnidadeMedida(models.Model):
    unidade_medida = models.CharField(max_length=50)
    abreviacao = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.unidade_medida} - {self.abreviacao}"
    
class Material(models.Model):
    TIPO_CHOICES = [
        ('materia_prima', 'Matéria-Prima'),
        ('produto_acabado', 'Produto Acabado'),
        ('embalagem', 'Embalagem'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=4, unique=True)
    descricao = models.TextField(blank=True)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Maquina(models.Model):
    nome_maquina = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    observacao = models.TextField(max_length=300)
    capacidade_producao = models.DecimalField(max_digits=10, decimal_places=2)
    em_manutencao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_maquina

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)
    matricula_funcionario = models.CharField(max_length=5)
    ativo = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_funcionario
