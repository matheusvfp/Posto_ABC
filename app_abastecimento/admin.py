from django.contrib import admin
from .models import Tanque, Bomba, Abastecimento


@admin.register(Tanque)
class TanqueAdmin(admin.ModelAdmin):
    list_display = ("tipo_combustivel", "data")
    search_fields = ("tipo_combustivel",)
    list_filter = ("tipo_combustivel",)


@admin.register(Bomba)
class BombaAdmin(admin.ModelAdmin):
    list_display = ("bomba_utilizada", "tanque")
    search_fields = ("bomba_utilizada",)
    list_filter = ("bomba_utilizada", "tanque__tipo_combustivel")


@admin.register(Abastecimento)
class AbastecimentoAdmin(admin.ModelAdmin):
    list_display = ("bomba", "data", "quantidade_litros", "valor_abastecido", "imposto")
    search_fields = ("bomba__bomba_utilizada",)
    list_filter = ("data", "bomba__tanque__tipo_combustivel")
