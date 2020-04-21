from django.contrib import admin
from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('equipes/', views.equipes, name='equipes'),
    path('admin/', admin.site.urls, name='admin'),
]
