from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')

def projetos(request):
    return render(request, 'projetos.html')
