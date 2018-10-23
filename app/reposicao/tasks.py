from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.test.signals import template_rendered
from django.core.mail import EmailMessage
from django.core import mail
from . import models
from . import views
connection = mail.get_connection()
connection.open()




@shared_task
def send_email(data_end,data, motivo, id):
    print ('objeto ola')
    pk = str('127.0.0.1:8000/reposicao/aceitar/%s')%id
    mensagen = str('Solicitacão de reposição de Aula \n Caro Coordenador, por meio desse email comunico que estarei ausente, pelo motivo de %s \n no período de %s à %s \n Para aceitar ou negar acesse o link : %s',)%(motivo, data, data_end, pk)
    email = mail.EmailMessage(
        'Solicitacao De reposição',
        mensagen,
        'carlosabc436@gmail.com',
        ['megatronstall@gmail.com'],
        connection=connection,)
    email.send()

connection.close()
