from django.db import models


class Produto(models.Model):
    sku = models.CharField(max_length=255)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome
