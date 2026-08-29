from django.urls import path

from . import views

urlpatterns = [
    path('livros/', views.lista_livros, name='lista livros'),
    path('livros/<int:id>/', views.detalhes_livro, name='detalhes_livro'),
    path('autor/', views.lista_autor, name='lista_autor'),
    path('autor/<int:id>/', views.detalhes_autor, name='detalhes_autor'),
]
