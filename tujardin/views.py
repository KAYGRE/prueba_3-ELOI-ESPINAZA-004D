import imp
from django.shortcuts import render, redirect
from .models import Producto
from .forms import formprod

# Create your views here.
def index(request):
    return render(request, 'index.html')
def empresa(request):
    return render(request, 'empresa.html')
def login(request):
    return render(request, 'login.html')
def products(request):
    return render(request, 'products.html')
def register(request):
    return render(request, 'register.html')
def clientform(request):
    return render(request, 'clientform.html')
def prodform(request):
    return render(request, 'prodform.html')