from django.contrib import admin
from django.urls import path, include
from producao import views as producao_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
    path('producao/', include('producao.urls')),
    path('', producao_views.index, name='index')
]
