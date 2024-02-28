from django.shortcuts import render
from arcanjo.models import Contact


def index(request):
    '''seleciona todos os contatos onde o campo show for true e
    mostrar em ordem decrescente'''
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {'contacts': contacts}

    print(contacts.query)

    return render(request, 'arcanjo/index.html', context)
