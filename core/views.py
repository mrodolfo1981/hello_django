from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))
def soma (request,a,b):
    r =a+b,
    return HttpResponse('<h2> A Soma de {} e {} é {} <h2>'.format(a,b,r))
def multiplicacao(request,a,b):
    r=a*b,
    return HttpResponse('<h2> A Multiplicação de {} por {} é {} <h2>'.format(a,b,r))
def divisao(request,a,b):
    r=a/b,
    return HttpResponse('<h2> A Divisão de {} por {} é {} <h2>'.format(a,b,r))
def subtracao (request,a,b):
    r =a-b,
    return HttpResponse('<h2> A Subtração de {} e {} é {} <h2>'.format(a,b,r))