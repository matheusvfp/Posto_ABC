from django.views.generic import ListView


from .models import Abastecimento


class AbastecimentosListView(ListView):
    model = Abastecimento
