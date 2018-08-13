
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Solicitacao, Autorizacao

class SolicitacaoForm(forms.ModelForm):
    user = forms.CharField(widgets=forms.HiddenField())
    def save(self, commit=True):
        solicitacao = super(SolicitacaoForm, self).save(commit=False)
        if commit:
            solicitacao.save()
        return solicitacao


    class Meta:
        model = Solicitacao

        fields = [
        'justification',
        'date_miss_start',
        'date_miss_end',
        'reason',
        'othes',
        'team',
        ]

        labels = {
        'justification': 'Justificativa:',
        'date_miss_start': 'Data inicial da falta:',
        'date_miss_end': 'Data final da falta:',
        'reason': 'Motivo:',
        'othes': 'Outro:',
        'team': 'Turma:',
        }

        widgets = {
        'justification': forms.TextInput(),
        'date_miss_start': forms.DateInput(),
        'date_miss_end': forms.DateInput(),
        'reason': forms.Select(),
        'othes': forms.TextInput(),
        'team': forms.Select(),
        }

class AutorizacaoForm(forms.ModelForm):
    def save(self, commit=True):
        Autorizacao = super(AutorizacaoForm, self).save(commit=False)
        if commit:
            Autorizacao.save()
        return Autorizacao

    status = forms.IntegerField(widgets=forms.HiddenField(), initial=1)
    justification_Aceit = forms.TextField(widgets=forms.TextField())
    class Meta:
        model = Autorizacao

        fields = ['status', 'justification_Aceit']
