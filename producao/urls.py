from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('new_ordem', views.nova_ordem_producao, name='new_ordem'),
    path('list_ordens', views.list_ordem_producao, name='list_ordens'),
    path('ordem_producao/<ordem_producao_id>/', views.ordem_de_producao, name='ordem_producao'),

]