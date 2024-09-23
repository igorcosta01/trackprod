from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('novo_produto', views.novo_produto, name='novo_produto'),
    path('list_produtos', views.list_produtos, name='list_produtos'),

]