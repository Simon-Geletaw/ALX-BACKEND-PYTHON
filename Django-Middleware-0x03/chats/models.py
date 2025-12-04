import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Role_choice = (('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin'))
    role = models.CharField(max_length=20, choices=Role_choice, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, unique=True, null=False)


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

