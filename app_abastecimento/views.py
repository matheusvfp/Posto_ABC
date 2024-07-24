from django.shortcuts import render
from .models import Abastecimento


def listar_abastecimentos(request):
    abastecimentos = Abastecimento.objects.all()
    return render(
        request, "listar_abastecimentos.html", {"abastecimentos": abastecimentos}
    )
