from django.shortcuts import render
from django.http import  HttpResponse

# Salom
def salom(request):
    return HttpResponse('Salom!')

# Salom sahifasini HTML shablob bilan oshish
def hello(request):
    return render(request, 'hello.html', {'ism': 'Diyorbek'})
