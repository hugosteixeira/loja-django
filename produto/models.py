from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=900)
    preco = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.ImageField(default='none.png', upload_to='')

    def __str__(self):
        return self.nome