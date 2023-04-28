from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Acessorio


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
