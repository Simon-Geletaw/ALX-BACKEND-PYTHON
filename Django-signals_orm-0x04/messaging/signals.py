
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db import models
from .models import Message, Notification, MessageHistory, User


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

@receiver(post_delete, sender=User)
def delete_suser_message(sender, instance, **kwargs):
    user = instance
    Message.objects.filter(sender=user.id).delete()
    MessageHistory.objects.filter(edited_by=user.id).delete()
    Notification.objects.filter(sender=user.id).delete()
    Notification.objects.filter(receiver=user.id).delete()
    
    
    