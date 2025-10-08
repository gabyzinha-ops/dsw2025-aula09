from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredientes(models.Model):
    nome = models.CharField(max_length=32)

    def __str__(self):
        return self.nome

import datetime

class Receitas(models.Model):
    titulo = models.CharField(max_length=64)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)


    ingredientes = models.ManyToManyField(                                                             
        to='Ingredientes',
        related_name='receitas',
        through='IngredienteReceita',
        through_fields=('receita', 'ingrediente')
    )

    @property
    def idade(self):
        return datetime.date.today().year - self.data_lancamento

    def __str__(self):
        return f'({self.id}) {self.titulo}'

class IngredienteReceita(models.Model):
    ingrediente = models.ForeignKey(
        to = Ingredientes,
        on_delete=models.CASCADE
    )
    receita = models.ForeignKey(
        to = Receitas,
        on_delete=models.CASCADE
    )

class Post(models.Model):
    autor = models.ForeignKey(
        to = User,
        on_delete = models.SET_NULL,
        null = True
    )
    imagem = models.ImageField(upload_to="posts/", blank=True, null=True)
    receita = models.TextField()
    aprovado = models.BooleanField(default=False)