from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from arcanjo.models import Contact


def index(request):
    '''seleciona todos os contatos onde o campo show for true e
    mostrar em ordem decrescente'''
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {'contacts': contacts, 'site_title': 'Contatos - '}

    # print(contacts.query)
    return render(request, 'arcanjo/index.html', context)


def search(request):
    '''realiza a busca do contato'''
    search_value = request.GET.get('q', '').strip()
    # print('search_value: ', search_value)
    if search_value == '':
        return redirect('arcanjo:index')

    contacts = Contact.objects. \
        filter(show=True). \
        filter(Q(first_name__icontains=search_value) |
               Q(last_name__icontains=search_value) |
               Q(phone__icontains=search_value) |
               Q(email__icontains=search_value)) \
        .order_by('-id')

    print(contacts.query)

    context = {'contacts': contacts, 'site_title': 'Contatos - '}
    # print(contacts.query)

    return render(request, 'arcanjo/index.html', context)


def contact(request, contact_id):
    '''retorna os dados de um contato via id (pk),
    caso o id não seja encontrado, ele retorna 404'''
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {'contact': single_contact, 'site_title': site_title}

    # print(single_contact.query)
    return render(request, 'arcanjo/contact.html', context)
