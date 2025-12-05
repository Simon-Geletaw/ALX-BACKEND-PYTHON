from models import Message
from django.db import models


class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        messages = self.filter(receiver=user, unread=True)
        if messages.exists():
            return messages
        else:
            return None