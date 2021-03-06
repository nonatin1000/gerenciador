"""gerenciador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^lista/$', 'agenda.views.lista'),
    url(r'^adiciona/$', 'agenda.views.adiciona'), 
    url(r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'), 
    url(r'^remove/(?P<nr_item>\d+)/$', 'agenda.views.remove'),  
    url(r'^login/', 'django.contrib.auth.views.login', {"template_name": "login.html"}),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', {"login_url": "/login/"}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]