from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>hello {} de {} anos de idade </h1>'.format(nome, idade))
