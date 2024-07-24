from django.contrib import admin
from django.urls import path

from app_abastecimento.views import AbastecimentosListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("listar/", AbastecimentosListView.as_view()),
]
