from django.shortcuts import render
from .models import Aluno

# Create your views here.
def listagem(request):
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'produtos/aluno/listagem.html', context)

def detalhes(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {'aluno': aluno}
    return render(request, 'produtos/aluno/detalhes.html', context)
