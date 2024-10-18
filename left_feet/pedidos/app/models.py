from django.db import models


class Pedido(models.Model):
    sku = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} - {self.data}"
