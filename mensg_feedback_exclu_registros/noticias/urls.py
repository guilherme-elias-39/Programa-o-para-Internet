
from django.urls import path
from . import views

urlpatterns = [
    path('lista_noticias/', views.lista_noticias, name='lista_noticias'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('detalhes_noticia/<int:id>', views.detalhes_noticia, name='detalhes_noticia'),
    path('lista_tags/', views.lista_tags, name='lista_tags'),
    path('categorias/cadastrar/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/<int:id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('tags/cadastrar/', views.cadastrar_tag, name='cadastrar_tag'),
    path('tags/<int:id>/editar/', views.editar_tag, name='editar_tag'),
    path('categorias/<int:id>/excluir/', views.excluir_categoria, name='excluir_categoria'),
    path('tags/<int:id>/excluir/', views.excluir_tag, name='excluir_tag'),    ]


