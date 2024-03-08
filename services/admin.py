from django.contrib import admin
from services import models


# Registrando um model na área admin do Django
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    # Dados visiveis no contacts
    list_display = ['id', 'project_name', 'status', 'project_url', 'server_name', 'server_ip',]
    ordering = '-id',
    search_fields = 'project_name', 'status', 'server_name', 'server_ip',
    list_per_page = 10
    list_max_show_all = 100
    # list_editable = ['first_name', 'last_name', 'show']
    list_display_links = 'id', 'project_name',


@admin.register(models.Category)
class CategoryProjectAdmin(admin.ModelAdmin):
    # Dados visiveis no contacts
    list_display = 'name',
    # Mostra os contatos na ordem decrescente
    ordering = '-id',


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    # Dados visiveis no contacts
    list_display = 'name',
    # Mostra os contatos na ordem decrescente
    ordering = '-id',

@admin.register(models.Ambiente)
class AmbienteProjectAdmin(admin.ModelAdmin):
    # Dados visiveis no contacts
    list_display = 'name',
    # Mostra os contatos na ordem decrescente
    ordering = '-id',
