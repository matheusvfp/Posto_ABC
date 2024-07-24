from django.db import models
from decimal import Decimal


class Tanque(models.Model):
    TIPO_COMBUSTIVEL = [
        ("GASOLINA", "Gasolina"),
        ("DIESEL", "Óleo Diesel"),
    ]

    tipo_combustivel = models.CharField(max_length=50, choices=TIPO_COMBUSTIVEL)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipo_combustivel


class Bomba(models.Model):
    BOMBAS_ASSOCIADAS_TANQUE = [
        ("GASOLINA 1", "Gasolina bomba 1"),
        ("GASOLINA 2", "Gasolina bomba 2"),
        ("DIESEL 1", "Diesel bomba 1"),
        ("DIESEL 2", "Diesel bomba 2"),
    ]

    tanque = models.ForeignKey(Tanque, related_name="bombas", on_delete=models.CASCADE)
    bomba_utilizada = models.CharField(max_length=50, choices=BOMBAS_ASSOCIADAS_TANQUE)

    def __str__(self):
        return f"Bomba: {self.bomba_utilizada} - Tanque: {self.tanque}"


class Abastecimento(models.Model):
    bomba = models.ForeignKey(
        Bomba, related_name="abastecimentos", on_delete=models.CASCADE
    )
    data = models.DateField(auto_now_add=True)
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)
    valor_abastecido = models.DecimalField(max_digits=10, decimal_places=2)
    imposto = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_imposto(self):
        return self.valor_abastecido * Decimal(0.13)

    def save(self, *args, **kwargs):
        # Ao salvar, calcular e atribuir o imposto
        self.imposto = self.calcular_imposto()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Abastecimento na bomba: {self.bomba.bomba_utilizada} - Tanque: {self.bomba.tanque.tipo_combustivel} em {self.data}"
