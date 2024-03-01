from django.shortcuts import render
from arcanjo.forms import ContactForm


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        # print(contacts.query)
        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm()
    }
    # print(contacts.query)
    return render(request, 'contact/create.html', context)
