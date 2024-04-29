from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
    path('pesquisadores/', views.pesquisadores, name='pesquisadores'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('lab/', views.lab, name='lab'),
    path('ps/', views.ps, name='ps'),
    path('leituras/', views.leituras, name='leituras'),
    path('oc/', views.oc, name='oc'),
    path('ocinfo/', views.ocinfo, name='ocinfo'),
]
