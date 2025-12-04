from rest_framework import serializers
from .models import User, Conversation, Message


class users(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'is_superuser',
                 'username', 'first_name', 'last_name', 'is_staff', 'is_active',
                 'date_joined', 'role', 'created_at', 'email', 'groups', 
                 'user_permissions']


class conversations(serializers.ModelSerializer):
    participants_id = users(many=True, read_only=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['participants_id']
        fields = "__all__"  # <-- REQUIRED

    def get_last_message(self, obj):
        last_msg = obj.messages.last()
        if last_msg:
            return messages(last_msg).data
        return None


class messages(serializers.ModelSerializer):
    participants = users(many=True, read_only=True)
    content = serializers.CharField(max_length=500)  

    class Meta:
        model = Message
        field = ['message_id', 'content', 'sent_at', 'sender_id']
        fields = "__all__" 
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty")
        return value
