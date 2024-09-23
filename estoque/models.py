from django.db import models
from apps.cadastro.models import Material

# Create your models here.

class MovimentoEstoque(models.Model):
    TIPO_MOVIMENTOS_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('ajuste', 'Ajuste'),
    ]

    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade_movimentada = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField()