from django.shortcuts import render

# Create your views here.
def lista_alunos(request):
    return render(request, 'alunos/lista_alunos.html')


