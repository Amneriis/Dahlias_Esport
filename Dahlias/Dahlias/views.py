from django.shortcuts import render
from django.urls import reverse


def accueil(request):
    return render(request, template_name='accueil.html')


def equipes(request):
    return render(request, 'equipes.html')
