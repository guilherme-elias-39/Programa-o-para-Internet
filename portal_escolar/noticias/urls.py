from django.urls import path
from . import views

urlpatterns = [
    path('lista_noticias/', views.lista_noticias, name='lista_noticias'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('detalhes_noticia/<int:id>', views.detalhes_noticia, name='detalhes_noticia'),
    path('lista_tags/', views.lista_tags, name='lista_tags'),
]

