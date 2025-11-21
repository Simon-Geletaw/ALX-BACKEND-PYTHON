import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messaging_app.settings")
django.setup()

from chats.models import User,Conversation,Message
from chats.serializers import Conversation,messages,users
