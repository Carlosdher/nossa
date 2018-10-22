# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.test.signals import template_rendered
# from django.core.mail import EmailMessage
# from django.core import mail
# from . import models, views, tasks
# connection = mail.get_connection()
# connection.open()
#
# def create_Solicitation(sender, instance, created, **kwargs):
#
#     if created:
#         models.Autorizacao.objects.create(solicitation = instance, status = 1)
#         lista = models.Autorizacao.objects.all()
#         tasks.send_email.delay(lista,instance)
#         # for objeto in lista:
#         #     if objeto.solicitation == instance:
#         #         pk = str('127.0.0.1:8000/reposicao/aceitar/%s') %objeto.pk
#         #         mensagen = str('Solicitacão de reposição de Aula \n Caro Coordenador, por meio desse email comunico que estarei ausente, pelo motivo de %s \n no período de %s à %s \n Para aceitar ou negar acesse o link : %s',)%(instance.reason,instance.date_miss_start,instance.date_miss_end,pk)
#
#         # email = mail.EmailMessage(
#         #     'Solicitacao De reposição',
#         #     mensagen,
#         #     'carlosabc436@gmail.com',
#         #     ['megatronstall@gmail.com'],
#         #     connection=connection,)
#         # email.send()
#         # connection.close()
#
#
# post_save.connect(create_Solicitation, sender=models.Solicitacao)
#
#
#
# def Autorizar(sender, instance, created, **kwargs):
#
#         if created:
#             pk = str('127.0.0.1:8000/reposicao/alterar/%s') %(instance.pk)
#             email = mail.EmailMessage(
#                 'Solicitacao Negada',
#                 pk,
#                 'carlosabc436@gmail.com',
#                 ['megatronstall@gmail.com'],
#                 connection=connection,)
#             email.send()
#             connection.close()
#             models.Autorizacao.objects.filter(id=instance.pk).update(status=(instance.status + 1))
#
#         if instance.status == 0:
#             pk = str('Caro discente sua Solicitacao de Reposicao foi negada pelos seguintes motivos:'
#             '\n \n \n %s'
#             '\n \n  Acesse o link para a alterações necessarias'
#             '\n \n \n 127.0.0.1:8000/reposicao/alterar/%s') %(instance.justification_Aceit, instance.pk)
#             email = mail.EmailMessage(
#                 'Solicitacao Negada',
#                 pk,
#                 'carlosabc436@gmail.com',
#                 ['megatronstall@gmail.com'],
#                 connection=connection,)
#             email.send()
#             connection.close()
#
#         elif (instance.status < 4):
#             pk = str('127.0.0.1:8000/reposicao/aceitar/%s') %(instance.pk)
#             email = mail.EmailMessage(
#                 'Hello',
#                 pk,
#                 'carlosabc436@gmail.com',
#                 ['carlosabc436@gmail.com'],
#                 connection=connection,)
#             email.send()
#             connection.close()
#             models.Autorizacao.objects.filter(id=instance.pk).update(status=(instance.status + 1))
#
#
# post_save.connect(Autorizar, sender=models.Autorizacao)
