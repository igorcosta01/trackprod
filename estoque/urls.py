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
    # path('entrada_estoque/<ordem_producao_id>/', views.entrada_estoque, name='entrada_estoque'),
    path('entrada_estoque_temp/', views.entrada_estoque_temp, name='entrada_estoque'),
    path("api/enderecos/", views.get_enderecos, name="api_enderecos"),







    path('list_estoque_intermediario', views.list_estoque_intermediario, name='list_estoque_intermediario'),
    path('entrada_estoque_intermediario', views.entrada_estoque_intermediario, name='entrada_estoque_intermediario'),
    path('produto_intermediario/<produto_intermediario_id>', views.produto_intermediario, name='produto_intermediario')
]