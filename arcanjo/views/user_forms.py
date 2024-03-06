from django.shortcuts import render, redirect
from arcanjo.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    form = RegisterForm()

    # messages.info(request, 'Mensagem de Informação!')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado!')
            return redirect('arcanjo:login')

    context = {'form': form}

    return render(request, 'contact/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('arcanjo:index')
        messages.error(request, 'Login inválido!')

    context = {'form': form}
    return render(request, 'contact/login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('arcanjo:login')


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != "POST":
        return render(request, 'contact/update-user.html', {'form': form})

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, 'contact/update-user.html', {'form': form})
    form.save()
    return redirect("arcanjo:user_update")
