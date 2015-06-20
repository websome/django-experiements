from django.conf.urls import url
from . import views
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<mitbringsel_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
