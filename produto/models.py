from django.db import models
from cliente.models import Cliente

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=900)
    preco = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.ImageField(default='none.png', upload_to='')

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    dataFinalizacao = models.DateField(blank=True,null=True)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=15,default=0)


class ItemCarrinho(models.Model):
    preco = models.DecimalField(decimal_places=2,max_digits=10)
    quantidade = models.IntegerField()
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Pedido,on_delete=models.CASCADE)
