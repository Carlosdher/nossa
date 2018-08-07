from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.core import mail
from . import models
connection = mail.get_connection()
connection.open()

def create_user_profile(sender, instance, created, **kwargs):

    if created:
        email = mail.EmailMessage(
            'Hello',
            'Body goes here',
            'carlosabc436@gmail.com',
            ['megatronstall@gmail.com'],
            connection=connection,
        )
        email.send()
        connection.close()

post_save.connect(create_user_profile, sender=models.Motivo)
