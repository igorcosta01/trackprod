from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse

# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'users/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            print(user)
            return HttpResponse('Já existe esse usuário.')
        
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()

    return HttpResponse("User cadastrado com sucesso.")


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))       
        else:
            return HttpResponse("Falha no login")
        
def logout_view(request):
    """Faz o logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

        