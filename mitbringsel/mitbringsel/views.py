from django.shortcuts import render
from django.http import Http404

from .models import Mitbringsel
from .forms import MitbringselForm
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'mitbringsel/index.html'
    context_object_name = 'mitbringsel_list'
    def get_queryset(self):
        return Mitbringsel.objects.all()

class AddView(generic.edit.CreateView):
    template_name = 'mitbringsel/form.html'
    form_class = MitbringselForm
    success_url = '/mitbringsel'