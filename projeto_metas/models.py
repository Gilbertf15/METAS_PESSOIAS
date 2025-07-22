from django.db import models

# Create your models here.

# model do usuario
class Users(models.Model):
    """MODELO DO USUARIO

    Args:
        models (_type_): _description_
    """
    username = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)



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


