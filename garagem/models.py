from django.db import models


class Marca(models.Model):
    """Marca de um veículo, como por exemplo: Fiat, Volkswagen, etc."""

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome.title()


class Categoria(models.Model):
    """Categoria de um veículo, como por exemplo: Carro, Moto, Caminhão, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()
