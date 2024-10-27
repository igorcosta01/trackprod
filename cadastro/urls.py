from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from producao import views as producao_views

urlpatterns = [

    path('new_ordem_modal', producao_views.nova_ordem_producao_modal, name='new_ordem_modal'),

    path('novo_produto/', views.novo_produto, name='novo_produto'),
    path('list_produtos/', views.list_produtos, name='list_produtos'),
    path('produto/<produto_id>', views.produto, name='produto'),
    
    path('list_funcionarios/', views.list_funcionarios, name='list_funcionarios'),
    path('novo_funcionario/', views.novo_funcionario, name='novo_funcionario'),
    

]