from django.contrib import admin
from django.urls import path

from app_abastecimento.views import (
    AbastecimentosListView,
    AbastecimentoCreateView,
    BombaCreateView,
    TanqueCreateView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", AbastecimentoCreateView.as_view(), name="abastecimento_create"),
    path("listar/", AbastecimentosListView.as_view(), name="abastecimento_list"),
    path("criar-tanques/", TanqueCreateView.as_view(), name="tanques_create"),
    path("criar-bombas/", BombaCreateView.as_view(), name="bombas_create"),
]
