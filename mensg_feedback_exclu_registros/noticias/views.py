
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Noticia, Categoria, Tag
from .forms import CategoriaForm, TagForm


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


def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'noticias/form_categoria.html', {'form': form, 'titulo': 'Cadastrar categoria' })


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'noticias/form_categoria.html', {'form': form, 'titulo': 'Editar categoria'})


def cadastrar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tag cadastrada com sucesso!')
            return redirect('lista_tags')
    else:
        form = TagForm()

    return render(request, 'noticias/form_tag.html', {'form': form, 'titulo': 'Cadastrar etiqueta'})


def editar_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tag atualizada com sucesso!')
            return redirect('lista_tags')
    else:
        form = TagForm(instance=tag)

    return render(request, 'noticias/form_tag.html', {'form': form, 'titulo': 'Editar etiqueta'})


from django.db.models.deletion import ProtectedError


def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(
                request,
                'Categoria excluída com sucesso!'
            )
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.'
            )

        return redirect('lista_categorias')

    return render(request, 'noticias/exclusao_categoria.html', {'categoria': categoria})


def excluir_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        tag.delete()
        messages.success(
            request,
            'Tag excluída com sucesso!'
        )
        return redirect('lista_tags')

    return render(
        request,'noticias/exclusao_tag.html', {'tag': tag})

