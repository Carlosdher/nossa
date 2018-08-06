from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from . import models

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(
            'Hello',
            'Body goes here',
            'megatronstall@gmail.com',
            ['carlosabc436@gmail.com',],
            [],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )

post_save.connect(create_user_profile, sender=models.Motivo)
