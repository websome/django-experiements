
from django.conf.urls import include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^mitbringsel/', include('mitbringsel.urls')),
    url(r'', include(frontend_urls)),
    url(r'^$', RedirectView.as_view(url='/mitbringsel', permanent=True)),
]
