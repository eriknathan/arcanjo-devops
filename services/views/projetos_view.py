from django.shortcuts import render
from services.forms import ProjetoForm
from services.models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projetos.html', context)


def create_project(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjetoForm()
    return render(request, 'projects/create.html', {'form': form})
