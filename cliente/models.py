from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50,unique=True)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome