# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url

from . import views as core




app_name = 'reposicao'

urlpatterns = [

    #Home
     path('reposicao/', core.Home.as_view(template_name='core/reposicao/home.html'), name='reposicao'),

     path('perfil/', core.Perfil.as_view(), name='perfil'),

     path('perfilup/<pk>/', core.PerfilUpdate.as_view(), name='perfilup'),

     #formulario de Reposição
     path('reposicao/formrep/', core.Reposicao.as_view(), name='formrep'),

     #formulario de Adiantamento de aula
     path('reposicao/formadianta/', core.Adiantamento.as_view(), name='formadianta'),

     path('reposicao/aceitar/<pk>/', core.Aceitar.as_view(), name='aceitar'),

     path('reposicao/aceitarform/<pk>/', core.AceitarCreateView.as_view(), name='aceitar-create'),

     path('reposicao/negarform/<pk>/', core.NegarCreateView.as_view(), name='negar-create'),


     path('reposicao/historico/', core.Historico.as_view(), name='historico'),

     path('teste/', core.Teste.as_view(), name="aa")


]
