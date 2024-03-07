from django.shortcuts import render, redirect
from django.urls import reverse
from services.forms import ProjetoForm
from services.models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projetos.html', context)


# def create_project(request):
#     if request.method == 'POST':
#         form = ProjetoForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ProjetoForm()
#     return render(request, 'projects/create.html', {'form': form})


def create_project(request):
    form_action = reverse('arcanjo:create')

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            print("Formulário é válido!")
            contact = form.save()
            return redirect('arcanjo:update', contact_id=contact.pk)

        # print(contacts.query)
        return render(request, 'contact/create.html', context)

    context = {
        'form': ProjetoForm(),
        'form_action': form_action,

    }
    # print(contacts.query)
    return render(request, 'projects/create.html', context)
