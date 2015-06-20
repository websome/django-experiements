from django.shortcuts import render
from django.http import Http404

from .models import Mitbringsel
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'mitbringsel/index.html'
    context_object_name = 'mitbringsel_list'
    def get_queryset(self):
        return Mitbringsel.objects.all()

class DetailView(generic.DetailView):
    model = Mitbringsel
    template_name = 'mitbringsel/detail.html'

