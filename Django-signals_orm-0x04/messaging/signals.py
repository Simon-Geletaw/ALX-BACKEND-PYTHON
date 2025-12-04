
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import Message, Notification


@receiver(post_save, sender=Message)
def _post_save_receiver(sender, **kwargs):
    message = Message.kwargs.get('instance')
    sender = message.sender
    receiver = message.receiver
    Notification.objects.create(
        sender=sender,
        receiver=receiver,
        notification_type="New Message"
    )
    
    
    