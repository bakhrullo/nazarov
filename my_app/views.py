from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def index(request):
    return render(request, 'my_app/index.html')


class Amal(ListView):
    model = Amaliyot
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'Amaliyot'}


class Oak(ListView):
    model = OAK
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'OAK'}


class Mar(ListView):
    model = Maruza
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'MARUZA'}


class Scop(ListView):
    model = Scopus
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'SCOPUS'}


class Mus(ListView):
    model = MustaqilTalim
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'MUSTAQIL TALIM'}


class Lab(ListView):
    model = Labartoriya
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'LABARATORIYA'}


class Konf(ListView):
    model = Konfirensiya
    context_object_name = 'files'
    template_name = "my_app/services.html"
    extra_context = {'title': 'KONFIRENSIYA'}
