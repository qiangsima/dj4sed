"""django4sed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^(?P<total>\d+)$', views.filter_total),
    url(r'^home$', views.home),
    url(r'^detail/(?P<timestamp>(\d|_)+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^search/$', views.news_search, name='archives'),
    url(r'^about_me/$', views.about_me, name='about_me'),
]
