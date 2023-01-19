from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hola hijos de su republica madre')
