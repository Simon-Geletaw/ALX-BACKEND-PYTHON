
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db import models
from .models import Message, Notification, MessageHistory


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
    
@receiver(pre_save, sender=Message)
def update_message_content_history(sender, instance, **kwargs):
    message = Message.kwargs.get('instance')
    user = message.sender
    old_content = message.content
    if Message.getattr('is_edited', sender=user):
        MessageHistory.objects.create(
            user=user,
            oldcontent=old_content
        )

    
    
    