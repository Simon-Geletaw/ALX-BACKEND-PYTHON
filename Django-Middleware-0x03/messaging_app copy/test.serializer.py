# test_serializers.py
import os
import django

# 1️⃣ Tell Python which Django settings to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messaging_app.settings")
django.setup()

# 2️⃣ Now you can import apps safely
from chats.models import User
from chats.serializers import users

# 3️⃣ Test serialization
user = User.objects.first()
serializer = users(user)
print(serializer.data)
