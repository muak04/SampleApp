"""crowdboticsTest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from crowdboticsApp.app_views.animals_views import animals_list, DogCreate, DogUpdate, CatCreate, CatUpdate
from crowdboticsApp.app_views.user_views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', animals_list, name="index"),
    url(r'^index/', animals_list, name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),

    url(r'dog/add/$', DogCreate.as_view(), name='dog-add'),
    url(r'dog/(?P<pk>[0-9]+)/$', DogUpdate.as_view(), name='dog-update'),

    url(r'cat/add/$', CatCreate.as_view(), name='cat-add'),
    url(r'cat/(?P<pk>[0-9]+)/$', CatUpdate.as_view(), name='cat-update'),

]
