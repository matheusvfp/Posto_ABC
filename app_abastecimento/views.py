from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


from .models import Abastecimento, Bomba, Tanque


class AbastecimentosListView(ListView):
    model = Abastecimento

class AbastecimentoCreateView(CreateView):
    model = Abastecimento
    fields = ["bomba", "quantidade_litros", "valor_abastecido"]
    success_url = reverse_lazy("abastecimento_list")
