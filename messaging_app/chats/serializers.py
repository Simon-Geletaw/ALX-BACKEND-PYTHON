from rest_framework import serializers
from chats.models import User, Conversation, Message


class users(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'is_superuser',
                 'username', 'first_name', 'last_name', 'is_staff', 'is_active',
                 'date_joined', 'role', 'created_at', 'email', 'groups', 
                 'user_permissions']


class conversations(serializers.ModelSerializer):
    participants_id = users(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'created_id', 'participants_id']


class messages(serializers.ModelSerializer):
    participants = users(many=True, read_only=True)
    
    class Meta:
        model = Message
        field = ['message_id', 'message_body', 'sent_at', 'sender_id']

         
   # Get a user instance
user = User.objects.first()

# Serialize
serializer = users(user)
print(serializer.data)     

