from rest_framework import serializers
from produtos.models import Produto
from users.serializers import UserSerializer
from spreadsheet import updateTotalProduto, updateProdutoDate

class ProdutoSerializer(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = '__all__'

    def get_usuario(self, obj):       
        return obj.user.nome

    def create(self, validated_data):
        produto = Produto.objects.create(**validated_data)

        cpf = validated_data['user'].cpf
        cadastroProduto = str(UserSerializer.get_first_date(self, validated_data['user']))
        totalProduto = UserSerializer.get_total_produtos(self, validated_data['user'])
        updateTotalProduto(cpf, totalProduto)
        updateProdutoDate(cpf, cadastroProduto)

        return produto

