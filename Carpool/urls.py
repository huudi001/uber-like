"""Carpool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
import app
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

from os import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^$', app.views.IndexView.as_view()),
    url('', include('app.urls')),



]

urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }))
