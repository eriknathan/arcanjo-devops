from django.contrib import admin
from arcanjo import models


# Registrando um model na área admin do Django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', # Dados visiveis no contacts
    ordering = '-id', # Mostra os contatos na ordem decrescente
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name', # realiza a pesquisa 
    list_per_page = 10 # Limita até 10 contatos na visualização
    list_max_show_all = 100 # Mostra tudo vai mostrar os últimos 100
    # list_editable = 'first_name', 'last_name'
    list_display_links = 'id', 'first_name', # acesso a parte de edição do contact



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', # Dados visiveis no contacts
    ordering = '-id', # Mostra os contatos na ordem decrescente
