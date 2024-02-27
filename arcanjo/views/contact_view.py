from django.shortcuts import render
from arcanjo.models import Contact

def index(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}

    return render(
        request, 'arcanjo/index.html', context
    )