from django.shortcuts import render

# Create your views here.


def accueil(request):
    return render(request, 'accueil.html')


def equipes(request):
    return render(request, 'equipes.html')
