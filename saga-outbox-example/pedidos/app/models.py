import uuid

from django.db import models


class Outbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=255)
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.topic} - {self.id}"


class Pedido(models.Model):
    sku = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} - {self.data}"
