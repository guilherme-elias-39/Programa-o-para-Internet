
from django import forms
from .models import Categoria, Tag



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome da categoria',
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['titulo']
        labels = {
            'titulo': 'Nome da etiqueta',
        }
