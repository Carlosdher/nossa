from django.dispatch import receiver
from django.core.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import EmailMessage



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(
            'Hello',
            'Body goes here',
            'megatronstall@gmail.com',
            ['carlosabc436@gmail.com', 'to2@example.com'],
            ['bcc@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
            )
