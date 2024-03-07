from django import forms
from . import models


class ProjetoForm(forms.ModelForm):
    project_name = forms.CharField(label='Nome do Projeto')
    category = forms.CharField(label='Categoria')
    status = forms.CharField(label='Status')
    technology = forms.CharField(label='Tecnologia')
    database = forms.CharField(label='Banco de Dados')
    project_url = forms.URLField(label='URL do Projeto')
    server_name = forms.CharField(label='Nome do Servidor')
    server_ip = forms.CharField(label='IP do Servidor')

    class Meta:
        model = models.Project
        fields = ('project_name', 'category', 'status', 'technology', 'database', 'project_url', 'server_name', 'server_ip',)
