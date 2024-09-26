from django.contrib import admin
from .models import OrdemProducao, ApontamentoProducao, Maquina

# Register your models here.

admin.site.register(OrdemProducao)
admin.site.register(ApontamentoProducao)
admin.site.register(Maquina)