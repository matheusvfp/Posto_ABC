from django.db import models
from django.utils import timezone


class Tanque(models.Model):
    TIPO_COMBUSTIVEL = [
        ("GASOLINA", "Gasolina"),
        ("DIESEL", "Óleo Diesel"),
    ]

    tipo_combustivel = models.CharField(max_length=50, choices=TIPO_COMBUSTIVEL)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo_combustive
