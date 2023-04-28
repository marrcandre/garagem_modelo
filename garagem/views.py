from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Acessorio, Cor, Veiculo
from garagem.serializers import (
    CategoriaSerializer,
    MarcaSerializer,
    AcessorioSerializer,
    CorSerializer,
    VeiculoSerializer
)


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

