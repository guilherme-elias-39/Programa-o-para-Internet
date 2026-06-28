from django.db import models

from django.db import models

# Create your models here.

class filmes(models.Model):
    titulo = models.CharField(max_length=100) #fixo
    lancamento = models.IntegerField()
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo
    

    

