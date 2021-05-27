from django.shortcuts import render
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
# from django.views.generic import ListView
from django.views import generic

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from users.serializers import UserSerializer
from spreadsheet import updateTotalProduto, updateProdutoDate


# Create your views here.

class ProdutoList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_destroy(self, instance):
        # import ipdb; ipdb.set_trace()
        instance.delete()

        cpf = instance.user.cpf
        cadastroProduto = str(UserSerializer.get_first_date(self, instance.user))
        totalProduto = UserSerializer.get_total_produtos(self, instance.user)
        updateTotalProduto(cpf, totalProduto)
        updateProdutoDate(cpf, cadastroProduto)
        
        
        # instance.delete()


