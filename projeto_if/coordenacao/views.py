from django.shortcuts import render, get_object_or_404
from .models import Projeto

# Create your views here.

def lista_projetos(request):
    projetos = Projeto.objects.all() #porque

    return render(request, 'coordenacao/lista_projetos.html', {'projetos': projetos})

def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    return render(request, 'coordenacao/detalhe_projeto.html', {'projeto': projeto}) #porque