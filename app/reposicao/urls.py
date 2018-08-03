# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from . import views as auth_views


app_name = 'reposicao'

urlpatterns = [
     path('reposicao/', auth_views.Home.as_view(template_name='core/reposicao/home.html'), name='reposicao'),
    # Login
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LoginView
    #path('', .Home.as_view()(template_name='templates/home.html'), name='home'),


]
