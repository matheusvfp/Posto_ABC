from django.test import TestCase
from decimal import Decimal
from app_abastecimento.models import Tanque, Bomba, Abastecimento


class TanqueTestCase(TestCase):
    def test_create_tanque_Gasolina(self):
        tanque = Tanque.objects.create(tipo_combustivel="GASOLINA")
        self.assertEqual(tanque.tipo_combustivel, "GASOLINA")
        self.assertIsNotNone(tanque.data)

    def test_tanque_str(self):
        tanque = Tanque.objects.create(tipo_combustivel="DIESEL")
        self.assertEqual(str(tanque), "DIESEL")


class BombaTestCase(TestCase):
    def setUp(self):
        self.tanque = Tanque.objects.create(tipo_combustivel="GASOLINA")

    def test_create_bomba(self):
        bomba = Bomba.objects.create(tanque=self.tanque, bomba_utilizada="GASOLINA 1")
        self.assertEqual(bomba.tanque, self.tanque)
        self.assertEqual(bomba.bomba_utilizada, "GASOLINA 1")

    def test_bomba_str(self):
        bomba = Bomba.objects.create(tanque=self.tanque, bomba_utilizada="GASOLINA 2")
        self.assertEqual(str(bomba), f"Bomba: GASOLINA 2 - Tanque: {self.tanque}")


class AbastecimentoTestCase(TestCase):
    def setUp(self):
        self.tanque = Tanque.objects.create(tipo_combustivel="GASOLINA")
        self.bomba = Bomba.objects.create(
            tanque=self.tanque, bomba_utilizada="GASOLINA 1"
        )

    def test_create_abastecimento(self):
        abastecimento = Abastecimento.objects.create(
            bomba=self.bomba, quantidade_litros=10, valor_abastecido=50
        )
        self.assertEqual(abastecimento.bomba, self.bomba)
        self.assertEqual(abastecimento.quantidade_litros, Decimal("10.00"))
        self.assertEqual(abastecimento.valor_abastecido, Decimal("50.00"))
        self.assertEqual(abastecimento.imposto, Decimal("6.50")) 

    def test_calcular_imposto(self):
        abastecimento = Abastecimento(bomba=self.bomba, valor_abastecido=100)
        self.assertEqual(abastecimento.calcular_imposto(), Decimal('13.00'))