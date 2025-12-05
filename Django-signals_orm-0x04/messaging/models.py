from django.db import models
from django.db.models.signals import post_save ,pre_save
from django.dispatch import receiver
from managers import UnreadMessagesManager


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)


class Notification(models.Model):
    sender = models.ForeignKey('Message', on_delete=models.CASCADE)
    receiver = models.ForeignKey('Message', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=100)
  
   
class Message(models.model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('User', on_delete=models.CASCADE)
    receiver = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', null=True, blank=True,
                                       on_delete=models.CASCADE)
    unread = models.BooleanField(default=False)
    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # Custom manager


class MessageHistory(models.Model):
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE)
    oldcontent = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    
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
