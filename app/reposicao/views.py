
# -*- coding: utf-8 -*-
from django.views.generic import View

from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse



from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models, forms, tasks
from django.shortcuts import render


from .teste import render_pdf


class Home(TemplateView):
    template_name = 'home.html'

class Lista(ListView):
    model = models.UUIDUser
    template_name = 'core/reposicao/tabela.html'

    def get_queryset(self):
        tasks.add.delay(1,2)
        if 'search' in self.request.GET:
            teachers = models.UUIDUser.objects.filter(first_name=self.request.GET['name'])
            return teachers
        else:
            return models.UUIDUser.objects.all()


class Perfil(ListView):
    model = models.UUIDUser
    template_name = 'core/reposicao/perfil.html'

class PerfilUpdate(UpdateView):
    model = models.UUIDUser
    template_name = 'core/user/formup.html'
    success_url = reverse_lazy('core:login')
    form_class = forms.UUIDUserForm


class Reposicao(CreateView):
    model = models.Solicitacao
    template_name = 'core/reposicao/formreposicao.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['date_miss_start','date_miss_end', 'justification', 'reason','othes','team']

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.usuario = self.request.user
         obj.save()
         return super(Reposicao, self).form_valid(form)
    def get_queryset(self):
        if 'sender' in self.request.POST:
            tasks.send_email.delay(model)
        return models.Solicitacao.objects.all()


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
    fields = ['status']




class NegarCreateView(UpdateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/negar.html'
    success_url = reverse_lazy('reposicao:reposicao')
    fields = ['status','justification_Aceit']


class Aceitar(UpdateView):
    model = models.Autorizacao
    template_name = 'core/reposicao/acite.html'
    fields = [ 'status', 'justification_Aceit']

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
        if 'search' in self.request.GET:
            kwargs['solicitacao'] = models.Solicitacao.objects.filter(usuario__first_name=self.request.user.first_name)
        else:
            kwargs['solicitacao'] = models.Solicitacao.objects.all()

        return super(Historico, self).get_context_data(**kwargs)

    def get_queryset(self):
        if 'search' in self.request.GET:
            information = models.Autorizacao.objects.filter(solicitation__usuario__first_name=self.request.user.first_name)
            return information
        else:
            if self.request.user.is_staff:
                information = models.Autorizacao.objects.all()
                return information
            else:
                information = models.Autorizacao.objects.filter(solicitation__usuario__first_name=self.request.user.first_name)
                return information



class Teste(View):
    def get(self, request, *args, **kwargs):
        dados = models.Solicitacao.objects.all()
        pdf = render_pdf("core/reposicao/as.html", {"dados": dados})
        return HttpResponse(pdf, content_type="application/pdf")










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
