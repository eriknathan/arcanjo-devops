from django import forms
from . import models


class ProjetoForm(forms.ModelForm):
    project_name = forms.CharField(label='Nome do Projeto')
    technology = forms.CharField(label='Tecnologia', required=False)
    database = forms.CharField(label='Banco de Dados', required=False)
    project_url = forms.URLField(label='URL do Projeto')
    

    class Meta:
        model = models.Project
        fields = ('project_name', 'category', 'ambiente', 'status', 'technology', 'database', 'project_url', 'server_name', 'server_ip',)
