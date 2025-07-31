from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    """_summary_

    Args:
        AbstractUser (_type_): _description_

    Returns:
        _type_: _description_
    """
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username



class Goal(models.Model):
    """ MODELO DE METAS DOS USUARIOS

    Args:
        models (_type_): _description_
    """
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    target_value = models.IntegerField()
    current_value = models.IntegerField()

    data_add = models.DateTimeField(auto_now_add=True)


