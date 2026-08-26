from django.urls import path, include
from . import views

app_name = 'aluno'

urlpatterns = [
    path('listaAlunos/', views.listagem, name='listaAlunos'),
    path('detalhesAluno/<int:id>/', views.detalhes, name='detalhesAluno'),
]