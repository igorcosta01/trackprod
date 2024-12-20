from django.contrib import admin
from .models import Material, ProdutoAcabado, MovimentoEstoqueAcabado, Drive

# Register your models here.

admin.site.register(Material)
admin.site.register(ProdutoAcabado)
admin.site.register(MovimentoEstoqueAcabado)
admin.site.register(Drive)
