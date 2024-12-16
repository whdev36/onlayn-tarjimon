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
    natijalar = ''
    s = request.GET.get('s', '')
    if s and s != '':
        natijalar = models.Lugat.objects.filter(ing__icontains=s).all()[:3] # 3 ta natijani olamiz!
    return render(request, 'index.html', {'s': s, 'natijalar': natijalar})
