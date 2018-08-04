# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from . import views as auth_views



app_name = 'reposicao'

urlpatterns = [

    #Home
     path('reposicao/', auth_views.Home.as_view(template_name='core/reposicao/home.html'), name='reposicao'),


     #formulario de Reposição
     path('reposicao/formrep/', auth_views.Reposicao, name='formrep'),


]
