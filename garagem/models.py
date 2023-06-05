from django.db import models


class Acessorio(models.Model):
    """Acessórios de um veículo, como por exemplo: Ar condicionado, Direção hidráulica, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()

    class Meta:
        verbose_name_plural = "Acessórios"
        verbose_name = "Acessório"


class Categoria(models.Model):
    """Categoria de um veículo, como por exemplo: Carro, Moto, Caminhão, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()


class Cor(models.Model):
    """Cor de um veículo, como por exemplo: Vermelho, Azul, etc."""

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()

    class Meta:
        verbose_name_plural = "Cores"


class Marca(models.Model):
    """Marca de um veículo, como por exemplo: Fiat, Volkswagen, etc."""

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome.upper()


class Modelo(models.Model):
    """Modelo de um veículo, como por exemplo: Gol, Uno, etc."""

    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.marca} {self.nome} {self.categoria}"


class Veiculo(models.Model):
    """Veículo, como por exemplo: Gol, Uno, etc."""

    descricao = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    acessorios = models.ManyToManyField(Acessorio)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )

    def __str__(self):
        return f" {self.ano} {self.cor}"

    class Meta:
        verbose_name_plural = "Veículos"
        verbose_name = "Veículo"
