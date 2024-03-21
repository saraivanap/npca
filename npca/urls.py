from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
    path('pesquisadores/', views.pesquisadores, name='pesquisadores'),
]
