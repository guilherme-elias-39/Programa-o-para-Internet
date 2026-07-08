
from django.urls import path, include
from . import views

app_name = 'destaques'

urlpatterns = [
    path('destaques/', views.destaques, name='destaques'),
    path('detalhes_des/<int:id>/', views.detalhes_destaques, name='detalhes_des')
]