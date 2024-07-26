from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.messages import get_messages
from decimal import Decimal
from app_abastecimento.models import Tanque, Bomba, Abastecimento


class TanqueCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy("tanques_create")

    def test_create_tanques(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tanque.objects.count(), 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Tanques criados com sucesso!")

    def test_tanques_already_exists(self):
        Tanque.objects.create(tipo_combustivel="GASOLINA")
        Tanque.objects.create(tipo_combustivel="DIESEL")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tanque.objects.count(), 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Tanques já existem.")


class BombaCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy("bombas_create")
        Tanque.objects.create(tipo_combustivel="GASOLINA")
        Tanque.objects.create(tipo_combustivel="DIESEL")

    def test_create_bombas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bomba.objects.count(), 4)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Bombas criadas com sucesso!")

    def test_bombas_already_exists(self):
        gasolina = Tanque.objects.get(tipo_combustivel="GASOLINA")
        diesel = Tanque.objects.get(tipo_combustivel="DIESEL")
        Bomba.objects.create(tanque=gasolina, bomba_utilizada="GASOLINA 1")
        Bomba.objects.create(tanque=gasolina, bomba_utilizada="GASOLINA 2")
        Bomba.objects.create(tanque=diesel, bomba_utilizada="DIESEL 1")
        Bomba.objects.create(tanque=diesel, bomba_utilizada="DIESEL 2")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bomba.objects.count(), 4)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Bombas já existem.")

    def test_tanques_not_exist(self):
        Bomba.objects.all().delete()
        Tanque.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Erro: É necessário criar os tanques primeiro."
        )


class AbastecimentosListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy("abastecimento_list")
        gasolina = Tanque.objects.create(tipo_combustivel="GASOLINA")
        diesel = Tanque.objects.create(tipo_combustivel="DIESEL")
        bomba_g1 = Bomba.objects.create(tanque=gasolina, bomba_utilizada="GASOLINA 1")
        bomba_d1 = Bomba.objects.create(tanque=diesel, bomba_utilizada="DIESEL 1")
        Abastecimento.objects.create(
            bomba=bomba_g1, quantidade_litros=10, valor_abastecido=50
        )
        Abastecimento.objects.create(
            bomba=bomba_d1, quantidade_litros=20, valor_abastecido=100
        )

    def test_list_abastecimentos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["object_list"]), 2)


class AbastecimentoCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy("abastecimento_create")
        gasolina = Tanque.objects.create(tipo_combustivel="GASOLINA")
        bomba_g1 = Bomba.objects.create(tanque=gasolina, bomba_utilizada="GASOLINA 1")
        self.bomba = bomba_g1

    def test_create_abastecimento(self):
        data = {
            "bomba": self.bomba.id,
            "quantidade_litros": 10,
            "valor_abastecido": 50,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Abastecimento.objects.count(), 1)
        abastecimento = Abastecimento.objects.first()
        self.assertEqual(abastecimento.bomba, self.bomba)
        self.assertEqual(abastecimento.quantidade_litros, Decimal("10.00"))
        self.assertEqual(abastecimento.valor_abastecido, Decimal("50.00"))
        self.assertEqual(abastecimento.imposto, Decimal("6.50"))
