from django.contrib import admin
from .models import Produto, UnidadeMedida, Material, Maquina, Funcionario

# Register your models here.

admin.site.register(Produto)
admin.site.register(UnidadeMedida)
admin.site.register(Material)
admin.site.register(Maquina)
admin.site.register(Funcionario)