from django.contrib import admin
from django.urls import path

from app_abastecimento.views import listar_abastecimentos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("listar/", listar_abastecimentos),
]
