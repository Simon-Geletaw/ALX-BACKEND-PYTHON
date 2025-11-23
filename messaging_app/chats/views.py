from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializers import messages
from .permissions import IsOwner

class MessageDetailView(APIView):
    permission_classes = [IsOwner]

    def get(self, request, pk):
        message = Message.objects.get(pk=pk)
        self.check_object_permissions(request, message)
        return Response(messages(message).data)
