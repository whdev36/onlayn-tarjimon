from django.shortcuts import render
from django.http import  HttpResponse

# Salom
def salom(request):
    return HttpResponse('Salom!')
