from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('new_ordem', views.nova_ordem_producao, name='new_ordem'),
    path('list_ordens', views.list_ordem_producao, name='list_ordens'),
    path('ordem_producao/<ordem_producao_id>/', views.ordem_de_producao, name='ordem_producao'),
    path('apontamento_producao/<ordem_producao_id>/', views.apontar_ordem_producao, name='apontamento_producao'),
    path('nova_maquina', views.nova_maquina, name='nova_maquina'),
    path('list_maquinas', views.list_maquinas, name='list_maquinas'),
    path('maquina/<maquina_id>', views.maquina, name='maquina'),
    path('edit_maquina/<maquina_id>', views.edit_maquina, name='edit_maquina'),
    path('api/dados_dashboard/', views.dados_dashboard, name='dados_dashboard'),

]