from django.db import models
from users.models import User

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(verbose_name='Produto', max_length=50)
    imagem = models.ImageField(upload_to='fileReceiver/', max_length=100)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey('users.User', related_name='UserProduto', on_delete=models.CASCADE)

    def __str__(self):
        return f'Produto: {self.nome}'

