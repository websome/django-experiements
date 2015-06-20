from django.conf.urls import url
from material.frontend import Module
from . import views

class Mitbringsel(Module):
    icon = 'mdi-image-compare'

    def get_urls(self):
        return [
            url(r'^$', views.IndexView.as_view(), name='index'),
            url(r'^new/$', views.AddView.as_view(), name='add'),
            #url(r'^(?P<mitbringsel_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        ]
