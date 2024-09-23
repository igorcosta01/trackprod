from django.contrib import admin
from .models import OrdemProducao, ApontamentoProducao

# Register your models here.

admin.site.register(OrdemProducao)
admin.site.register(ApontamentoProducao)