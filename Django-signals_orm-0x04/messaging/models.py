from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)


class Notification(models.Model):
    sender = models.ForeignKey('Message', on_delete=models.CASCADE)
    receiver = models.ForeignKey('Message', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=100)
  
   
class Message(models.model):
    sender = models.ForeignKey('User', on_delete=models.CASCADE)
    receiver = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

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
    
    
    
    
