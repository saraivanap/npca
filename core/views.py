from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')

def projetos(request):
    return render(request, 'projetos.html')

def contato(request):
    return render(request, 'contato.html')

def pesquisadores(request):
    return render(request, 'pesquisadores.html')

def publicacoes(request):
    return render(request, 'publicacoes.html')