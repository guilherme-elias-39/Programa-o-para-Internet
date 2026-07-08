
from django.urls import path
from . import views

app_name = 'lista_lancamentos'

urlpatterns = [
    path('lista/', views.lancamentos, name='lista'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes')
    
]

