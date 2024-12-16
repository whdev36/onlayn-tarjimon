from django.shortcuts import render
from django.http import  HttpResponse
from . import models

# Salom
def salom(request):
    return HttpResponse('Salom!')

# Salom sahifasini HTML shablon bilan oshish
def hello(request):
    return render(request, 'hello.html', {'ism': 'Diyorbek'})

# Bosh sahifani yaratish
def index(request):
    s = request.GET.get('s', '')
    return render(request, 'index.html', {'s': s})
