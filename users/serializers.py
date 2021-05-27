from rest_framework import serializers
from users.models import User
# from django.http import HttpResponseForbidden
from django.contrib.auth.validators import UnicodeUsernameValidator
from produtos.models import Produto
from rest_framework import generics, status
from rest_framework.response import Response
from spreadsheet import createUser, updateUser

class UserSerializer(serializers.ModelSerializer):
    total_produtos = serializers.SerializerMethodField()
    first_date = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username','nome','password', 'data_nascimento', 'cpf', 'created_at','UserProduto', 'total_produtos', 'first_date'  ) #
        # extra_kwargs = { #remove a validação do user.username para o PUTrequest
        #     'username': {
        #         'validators': [UnicodeUsernameValidator()],
        #     },
        # }

    def get_total_produtos(self, obj):
        # import ipdb; ipdb.set_trace()
        valor = Produto.objects.filter(user=obj).count()
        return valor

    def get_first_date(self, obj):
        # import ipdb; ipdb.set_trace()
        if obj.UserProduto.values():
            date = obj.UserProduto.values()[0].get('created_at')
            return date
        else:
            return None 

    def create(self, validated_data):
        
        nome = validated_data['nome']
        data_nascimento= validated_data['data_nascimento']
        cpf= validated_data['cpf']

        user = User.objects.create( 
            username = validated_data['username'],
            nome = nome,
            data_nascimento = data_nascimento,
            cpf = cpf,
        )
        user.set_password(validated_data['password'])

        # import ipdb; ipdb.set_trace()
        created_at = str(user.created_at)
        nascimento = str(data_nascimento) #temporário pois preciso do get_idade
        list = [nome, cpf, nascimento, created_at]
        createUser(list)

        user.save()
        return user

    def update(self, instance, validated_data):
        nome = validated_data['nome']
        nascimento = validated_data['data_nascimento']
        cpf= validated_data['cpf']
        created_at = str(instance.created_at)
        cadastroProduto = str(UserSerializer.get_first_date(self, instance))
        totalProduto = UserSerializer.get_total_produtos(self, instance)

        list = [nome, cpf, nascimento, created_at, cadastroProduto, totalProduto]
        # updateUser(cpf, list)

        #cadastro do primeiro produto
        #instance.UserProduto.values()[0].get('created_at')

        #total de produtos
        #Produto.objects.filter(user = instance).count()

        # import ipdb; ipdb.set_trace()
        instance.username = validated_data['username']
        instance.nome = nome
        instance.set_password(validated_data['password'])
        instance.data_nascimento = nascimento
        instance.cpf = cpf
        instance.save()
    
        return instance

    
    

    


