from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    """Index da aplicação"""
    return render(request, 'core/index.html')