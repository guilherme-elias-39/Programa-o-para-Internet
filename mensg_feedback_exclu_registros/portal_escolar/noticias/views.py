from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def lista_noticias(request):
    noticias = Noticia.objects.all()

    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all()

    return render(request, 'noticias/lista_categorias.html', {'categorias': categorias, 'noticias': noticias})

def detalhes_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    return render(request, 'noticias/detalhes_noticia.html', {'noticia': noticia})

def lista_tags(request):
    tags = Tag.objects.all()
    noticias = Noticia.objects.all()

    return render(request, 'noticias/lista_tags.html', {'tags': tags, 'noticias': noticias})