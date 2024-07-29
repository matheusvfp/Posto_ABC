from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Abastecimento, Bomba, Tanque


class TanqueCreateView(View):
    def get(self, request):
        if not Tanque.objects.exists():
            Tanque.objects.create(tipo_combustivel="GASOLINA")
            Tanque.objects.create(tipo_combustivel="DIESEL")
            messages.success(request, "Tanques criados com sucesso!")
        else:
            messages.info(request, "Tanques já existem.")
        return HttpResponseRedirect(reverse_lazy("abastecimento_create"))


class BombaCreateView(View):
    def get(self, request):
        try:
            if not Bomba.objects.exists():
                gasolina = Tanque.objects.get(tipo_combustivel="GASOLINA")
                diesel = Tanque.objects.get(tipo_combustivel="DIESEL")
                Bomba.objects.create(tanque=gasolina, bomba_utilizada="GASOLINA 1")
                Bomba.objects.create(tanque=gasolina, bomba_utilizada="GASOLINA 2")
                Bomba.objects.create(tanque=diesel, bomba_utilizada="DIESEL 1")
                Bomba.objects.create(tanque=diesel, bomba_utilizada="DIESEL 2")
                messages.success(request, "Bombas criadas com sucesso!")
            else:
                messages.info(request, "Bombas já existem.")
        except Tanque.DoesNotExist:
            messages.error(request, "Erro: É necessário criar os tanques primeiro.")
        return HttpResponseRedirect(reverse_lazy("abastecimento_create"))


class AbastecimentosListView(ListView):
    model = Abastecimento
    queryset = Abastecimento.objects.all()


class AbastecimentoCreateView(CreateView):
    model = Abastecimento
    fields = ["bomba", "quantidade_litros", "valor_abastecido"]
    success_url = reverse_lazy("abastecimento_list")

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, "Abastecimento criado com sucesso!")
        return redirect(self.get_success_url())
