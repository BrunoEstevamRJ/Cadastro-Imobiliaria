from django.db import models


class Clientes(models.Model):
    cliente = models.CharField(max_length=255)
    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.cliente
