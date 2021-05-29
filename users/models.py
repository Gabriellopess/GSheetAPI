from django.db import models
from django.contrib.auth.models import AbstractUser, User
from cpf_field.models import CPFField
from django.utils.translation import gettext_lazy as _


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from datetime import date

class User(AbstractUser):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(default = '2000-01-01')
    cpf = CPFField('cpf', unique=True)
    email = models.EmailField(_('email address'), blank=True)
    created_at = models.DateField(auto_now_add=True)
    

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
            return f'User {self.pk} | {self.nome}'
