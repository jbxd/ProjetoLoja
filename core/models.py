from django.db import models

class Produtos(models.Model):
    nome = models.CharField('x-tudo', max_length = 100)
    preco = models.DecimalField('Valor', decimal_places = 2, max_digits = 5)

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=50)
    sobrenome = models.CharField('sobrenome', max_length=50)
    endereco = models.CharField('endereço', max_length= 100)
    def __str__(self):
        return self.nome

class Lanches1(models.Model):
    produto = models.CharField('Produto', max_length=50)
    valor = models.DecimalField('valor', decimal_places=2, max_digits=10)
    def __str__(self):
        return self.produto