from django.contrib import admin
from django.urls import path

from app_abastecimento.views import AbastecimentosListView, AbastecimentoCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", AbastecimentoCreateView.as_view(), name="abastecimento_create"),
    path("listar/", AbastecimentosListView.as_view(), name="abastecimento_list"),
]
