from django.db import models
from django.contrib.auth.models import User ########

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class PerfilAcademico(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    link_lattes = models.URLField()
    biografia = models.TextField()

    def __str__(self):
        return f"Perfil de {self.aluno.nome}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    equipe = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.titulo