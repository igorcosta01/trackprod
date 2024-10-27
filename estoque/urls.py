from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # path('new_ordem', views.nova_ordem_producao, name='new_ordem'),
    path('list-produto-acabado', views.list_produto_acabado, name='list-produto-acabado'),
    path('produto_acabado/<produto_acabado_id>/', views.produto_acabado, name='produto_acabado'),
]