from django.shortcuts import render

# Create your views here.

def lista(request):
    return render(request, 'livros/lista.html')

def detalhes(request):
    return render(request, 'livros/detalhes.html')