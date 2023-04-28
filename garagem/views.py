from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Acessorio
from garagem.serializers import (
    CategoriaSerializer,
    MarcaSerializer,
    AcessorioSerializer,
)


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
