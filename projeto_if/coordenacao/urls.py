from django.urls import path
from . import views

urlpatterns = [
    path('lista_projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:id>/', views.detalhe_projeto, name='detalhe_projeto'),
    
]
