from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Role_choice = (('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin'))
    role = models.CharField(max_length=20, choices=Role_choice, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, unique=True, null=False, )
    first_name
    last_name
    password
    user_id
    phone_number


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, null=False, db_index=True)
    sender_id = models.ForeignKey(User(id), on_delete=models.CASCADE)
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, db_index=True)
    participants_id = models.ForeignKey(User(id), on_delete=models.CASCADE)
    created_id = models.DateTimeField(auto_now_add=True)


