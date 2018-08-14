
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

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.user = self.request.user
         obj.save()
         return super(Reposicao, self).form_valid(form)

class AceitarCreateView(CreateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/aceitar.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['status']

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.user = self.request.user
         obj.save()
         return super(AceitarCreateView, self).form_valid(form)

class NegarCreateView(CreateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/negar.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['status','justification_Aceit']

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.user = self.request.user
         obj.save()
         return super(NegarCreateView, self).form_valid(form)

class Aceitar(DetailView):
    model = models.Autorizacao
    template_name = 'core/reposicao/acite.html'
    def get_queryset(self):
        return models.Solicitacao.objects.all()


class Historico(ListView):
    model = models.Autorizacao
    template_name = 'core/reposicao/historico.html'
    def get_queryset(self):
        return models.Solicitacao.objects.all()








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
