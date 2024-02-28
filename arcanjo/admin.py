from django.contrib import admin
from arcanjo import models


# Registrando um model na área admin do Django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Dados visiveis no contacts
    list_display = ['id', 'first_name', 'last_name', 'phone', 'show']
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    # list_editable = ['first_name', 'last_name', 'show']
    list_display_links = 'id', 'first_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # Dados visiveis no contacts
    list_display = 'name',
    # Mostra os contatos na ordem decrescente
    ordering = '-id',
