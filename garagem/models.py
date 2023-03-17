from django.db import models


class Marca(models.Model):
    """Marca de um veículo, como por exemplo: Fiat, Volkswagen, etc."""

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    """Categoria de um veículo, como por exemplo: Carro, Moto, Caminhão, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()


class Acessorio(models.Model):
    """Acessórios de um veículo, como por exemplo: Ar condicionado, Direção hidráulica, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()
    
    class Meta:
        verbose_name_plural = "acessórios"
        verbose_name = "acessório"


class Cor(models.Model):
    """Cor de um veículo, como por exemplo: Vermelho, Azul, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()
    
    class Meta:
        verbose_name_plural = "cores"


class Veiculo(models.Model):
    """Veículo, como por exemplo: Gol, Uno, etc."""

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} - {self.cor}"

    class Meta:
        verbose_name_plural = "veículos"
        verbose_name = "veículo"