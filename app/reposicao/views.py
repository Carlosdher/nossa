
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from .models import Solicitacao
from .form import SolicitacaoForm

from django.shortcuts import render

class Home(TemplateView):
    template_name = 'home.html'

class Reposicao(CreateView):
    model = Solicitacao
    form_class = SolicitacaoForm
    template_name = 'core/reposicao/formreposicao.html'

def historico(request):
    template_name = 'core/reposicao/historico.html'
    return render(request,template_name)

def adiantamento(request):
    template_name = 'core/reposicao/formadiantamento.html'
    return render(request,template_name)

def troca(request):
    template_name = 'core/reposicao/formtroca.html'
    return render(request,template_name)
