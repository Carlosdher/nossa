
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models



class Home(TemplateView):
    template_name = 'home.html'

class Reposicao(CreateView):
    model = models.Solicitacao
    template_name = 'core/reposicao/formreposicao.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['date_miss_start','date_miss_end', 'justification', 'reason','othes','team']


class Aceitar(DetailView):
    model = models.Solicitacao
    template_name = 'core/reposicao/acite.html'


    # def get_context_data(self, **kwargs):
    #     kwargs['categories'] = models.Category.objects.all()
    #
    #     return super(BooksView, self).get_context_data(**kwargs)
    #
    # def get_queryset(self):
    #     if 'category' in self.request.GET:
    #         return models.Book.objects.filter(category=self.request.GET['category'])
    #     return models.Book.objects.all()




#def historico(request):
#    template_name = 'core/reposicao/historico.html'
#    return render(request,template_name)
#
#def adiantamento(request):
#    template_name = 'core/reposicao/formadiantamento.html'
#    return render(request,template_name)

#def troca(request):
#    template_name = 'core/reposicao/formtroca.html'
#    return render(request,template_name)
