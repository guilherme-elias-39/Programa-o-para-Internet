from django.shortcuts import render
from .models import Livro, Autor

# Create your views here.


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/lista_livros.html', {'livros': livros})


def detalhes_livro(request, id):
    livros = Livro.objects.all()

    for livro in livros:
        if livro.id == id:
            livro_selecionado = livro
            break

    return render(request, 'acervo/detalhes_livro.html', {'livro': livro_selecionado})


def lista_autor(request):
    autores = Autor.objects.all()
    return render(request, 'acervo/lista_autor.html', {'autores': autores})


def detalhes_autor(request, id):
    autores = Autor.objects.all()

    for autor in autores:
        if autor.id == id:
            autor_selecionado = autor
            break

    return render(request, 'acervo/detalhes_autor.html', {'autor': autor_selecionado})