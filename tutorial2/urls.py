from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', include('snippets.urls')),
    url(r'^',include('snippets.apiview_urls')),
    # url(r'^', include('snippets.mixins_urls')),
    # url(r'^', include('snippets.generics_urls')),
]
