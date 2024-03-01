from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from arcanjo.forms import ContactForm
from arcanjo.models import Contact


def create(request):
    form_action = reverse('arcanjo:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)

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
        'form': ContactForm(),
        'form_action': form_action,

    }
    # print(contacts.query)
    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    form_action = reverse('arcanjo:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

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
        'form': ContactForm(instance=contact),
        'form_action': form_action,

    }
    # print(contacts.query)
    return render(request, 'contact/create.html', context)
