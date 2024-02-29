from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from arcanjo.models import Contact
from django.core.paginator import Paginator


def create(request):
    context = {}
    # print(contacts.query)
    return render(request, 'contact/create.html', context)
