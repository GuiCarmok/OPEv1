from django.db import models

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.FloatField()
    quantidade = models.IntegerField()
