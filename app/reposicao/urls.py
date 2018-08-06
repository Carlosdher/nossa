# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url

from . import views as core




app_name = 'reposicao'

urlpatterns = [

    #Home
     path('reposicao/', core.Home.as_view(template_name='core/reposicao/home.html'), name='reposicao'),
     path('perfil/<pk>/', core.Perfil.as_view(template_name='core/reposicao/perfil.html'), name='perfil'),


     #formulario de Reposição
     path('reposicao/formrep/', core.Reposicao.as_view(), name='formrep'),


]
