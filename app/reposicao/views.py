
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models



class Home(TemplateView):
    template_name = 'home.html'

class Perfil(UpdateView):
    model = models.UUIDUser
    template_name = 'core/reposicao/perfil.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['first_name', 'last_name', 'password', 'email', 'cpf', 'registration', 'picture']
    

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

class Adiantamento(CreateView):
    model = models.Solicitacao
    template_name = 'core/reposicao/formadiantamento.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['date_miss_start','date_miss_end', 'justification', 'reason','othes','team']

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.user = self.request.user
         obj.save()
         return super(Adiantamento, self).form_valid(form)



class AceitarCreateView(UpdateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/aceitar.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['status', 'solicitation']


class NegarCreateView(UpdateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/negar.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['status','justification_Aceit', 'solicitation']


class Aceitar(UpdateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/acite.html'
    fields = [ 'status', 'justification_Aceit', 'solicitation']

    def get_context_data(self, **kwargs):
        kwargs['solicitacao'] = models.Solicitacao.objects.all()
        return super(Aceitar, self).get_context_data(**kwargs)

    def get_queryset(self):
        return models.Autorizacao.objects.all()

class Historico(ListView):
    model = models.Autorizacao
    template_name = 'core/reposicao/historico.html'


    def get_context_data(self, **kwargs):
        kwargs['Planejamento'] = models.Planejamento.objects.all()
        kwargs['solicitacao'] = models.Solicitacao.objects.all()

        return super(Historico, self).get_context_data(**kwargs)

    def get_queryset(self):
        return models.Autorizacao.objects.all()








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
