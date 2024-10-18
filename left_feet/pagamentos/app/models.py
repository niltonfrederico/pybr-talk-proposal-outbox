from django.db import models


class Pagamento(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.nome
