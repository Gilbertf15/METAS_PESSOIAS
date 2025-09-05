from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Users(AbstractUser):
    """MODELO DA TABELA USUARIOS"""

    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username

class Goal(models.Model):
    """ MODELO DE METAS DOS USUARIOS """

    CLASSIFICACAO_META = [
        (1, 'importante'),
        (2, 'intermediario'),
        (3, 'não importante'),
    ]
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    target_value = models.IntegerField(choices=CLASSIFICACAO_META) # campo classificação
    current_value = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)]) # campo progressso

    data_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


