from django.shortcuts import render, redirect
from arcanjo.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()

    # messages.info(request, 'Mensagem de Informação!')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado!')
            return redirect('arcanjo:index')


    context = {'form': form}

    return render(request, 'contact/register.html', context)
