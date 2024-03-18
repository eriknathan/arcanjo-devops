from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from services.forms import ProjetoForm
from services.models import Project
import docker


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects,  'site_title': 'Projetos - '}
    return render(request, 'projects/projetos.html', context)


def project(request, project_id):
    '''retorna os dados de um contato via id (pk),
    caso o id não seja encontrado, ele retorna 404'''
    single_project = get_object_or_404(Project, pk=project_id)

    site_title = f'{single_project.project_name} - '
    context = {'project': single_project, 'site_title': site_title}

    # print(single_contact.query)
    return render(request, 'projects/projeto.html', context)


def create_project(request):
    form_action = reverse('services:create')

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            print("Formulário é válido!")
            project = form.save()
            return redirect('services:update', project_id=project.pk)

        # print(contacts.query)
        return render(request, 'projects/create.html', context)

    context = {
        'form': ProjetoForm(),
        'form_action': form_action,

    }
    # print(contacts.query)
    return render(request, 'projects/create.html', context)


def update(request, project_id):
    project = get_object_or_404(
        Project, pk=project_id
    )
    form_action = reverse('services:update', args=(project_id,))

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=project)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            print("Formulário é válido!")
            project = form.save()
            return redirect('services:update', project_id=project.pk)

        # print(project.query)
        return render(request, 'projects/create.html', context)

    context = {
        'form': ProjetoForm(instance=project),
        'form_action': form_action,

    }
    # print(contacts.query)
    return render(request, 'projects/create.html', context)


def delete(request, contact_id):
    project = get_object_or_404(
        Project, pk=contact_id
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        project.delete()
        return redirect('services:projects')

    return render(
        request,
        'projects/projeto.html',
        {
            'project': project,
            'confirmation': confirmation,
        }
    )


def docker_list(request):
    client = docker.from_env()
    containers = client.containers.list()

    container_info = []
    for container in containers:
        container_info.append({
            "Nome": container.name,
            "Status": container.status,
            "ID": container.short_id,
            "Imagem": container.image.tags[0] if container.image.tags else "",
            # "Comando": container.attrs['Config']['Cmd'] if 'Cmd' in container.attrs['Config'] else "",
            # "Portas": container.ports
        })

    context = {'containers': container_info}

    return render(request, 'projects/container_list.html', context)
