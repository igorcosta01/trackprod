from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # path('new_ordem', views.nova_ordem_producao, name='new_ordem'),
    path('list-produto-acabado', views.list_produto_acabado, name='list-produto-acabado'),
    path('produto_acabado/<produto_acabado_id>/', views.produto_acabado, name='produto_acabado'),
    path('mov_estoque_acabado', views.mov_estoque_acabado, name='mov_estoque_acabado'),
    path('novo_produto_acabado', views.novo_produto_acabado, name='novo_produto_acabado'),
    path('ordens_producao_finalizadas/', views.ordens_producao_entrada_estoque, name='ordens_producao_entrada_estoque'),
]