from django.contrib import admin
from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('lista/', views.lista, name='lista'),
    path('detalhes/', views.detalhes, name='detalhes'),
]
