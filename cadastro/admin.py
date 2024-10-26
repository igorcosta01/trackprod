from django.contrib import admin
from .models import Produto, UnidadeMedida, Funcionario, Cliente

# Register your models here.

admin.site.register(Produto)
admin.site.register(UnidadeMedida)
admin.site.register(Funcionario)
admin.site.register(Cliente)