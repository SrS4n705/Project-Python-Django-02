from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Joelio Santos'
    })


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return render(request, 'recipes/contato.html')
