from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Message, Conversation
from .serializers import messages, conversations
from .permissions import IsOwner

# ------------------------------
# Messages
# ------------------------------

class MessageListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Return only messages where the user is the sender
        messages = Message.objects.filter(sender=request.user)
        serializer = messages(messages, many=True)
        return Response(serializer.data)


class MessageDetailView(APIView):
    ##permission_classes = [IsAuthenticated, IsOwner]
    def get(self, request, pk):
        message = get_object_or_404(Message, pk=pk)
        self.check_object_permissions(request, message)
        serializer = messages(message)
        return Response(serializer.data)


# ------------------------------
# Conversations
# ------------------------------

class ConversationListView(APIView):
    ##permission_classes = [IsAuthenticated]

    def get(self, request):
        # Return only conversations where the user is a participant
        conversations = Conversation.objects.filter(participants=request.user)
        serializer = conversations(conversations, many=True)
        return Response(serializer.data)


class ConversationDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        self.check_object_permissions(request, conversation)
        serializer = conversations(conversation)
        return Response(serializer.data)
