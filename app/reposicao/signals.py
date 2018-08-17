from django.dispatch import receiver
from django.db.models.signals import post_save
from django.test.signals import template_rendered
from django.core.mail import EmailMessage
from django.core import mail
from . import models
from . import views
connection = mail.get_connection()
connection.open()

def create_Solicitation(sender, instance, created, **kwargs):

    if created:
        models.Autorizacao.objects.create(solicitation = instance, status = 1)
        pk = str('127.0.0.1:8000/reposicao/aceitar/%s') %instance.pk
        email = mail.EmailMessage(
            'Hello',
            pk,
            'carlosabc436@gmail.com',
            ['megatronstall@gmail.com'],
            connection=connection,)
        email.send()
        connection.close()
        models.Autorizacao.objects.create(solicitation = instance, status = 1)

post_save.connect(create_Solicitation, sender=models.Solicitacao)



def Autorizar(sender, instance, created, **kwargs):

    if created:
        pk = str('Caro discente sua Solicitacao de Reposicao foi negada pelos seguintes motivos:'
         '\n \n \n %s'
         '\n \n  Acesse o link para a alterações necessarias'
         '\n 127.0.0.1:8000/reposicao/alterar/%s') %(instance.justification_Aceit, instance.pk)
        if instance.status == 0:
            email = mail.EmailMessage(
                'Solicitacao Negada',
                pk,
                'carlosabc436@gmail.com',
                ['carlosabc436@gmail.com'],
                connection=connection,)
            email.send()
            connection.close()

        elif instance.status == 2:
            pk = str('127.0.0.1:8000/reposicao/aceitar/%s') %instance.pk
            email = mail.EmailMessage(
                'Hello',
                pk,
                'carlosabc436@gmail.com',
                ['carlosabc436@gmail.com'],
                connection=connection,)
            email.send()
            connection.close()

post_save.connect(Autorizar, sender=models.Autorizacao)
