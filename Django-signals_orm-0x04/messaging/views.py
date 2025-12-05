from django.http import HttpResponse, JsonResponse
from .models import Message,  User
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .models import Message,  User
from django.db.models import Q
from managers import UnreadMessagesManager


[sender=request.user, receiver]
class delete_user:
    def post(self, request, user_id):
        user = request.user
        if user.id != user_id:
            return HttpResponse("Unauthorized", status=401)
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return HttpResponse("User and related data deleted successfully", status=200)
        except User.DoesNotExist:
            return HttpResponse("User not found", status=404)


class get_text_message:
    def build_thread(self, message):
        return {
            "id": message.id,
            "body": message.content,
            "timestamp": message.created_at,
            "is_edited": message.is_edited,
            "replies": [self.build_thread(reply) for reply in message.replies.all()],
        }

    def get(self, request, sender_id, reciever_id):
        user =request.user
        messages = (
            Message.objects.filter(
                Q(sender_id=user, reciever_id=reciever_id)
                | Q(sender_id=reciever_id, reciever_id=user)
            )
            .select_related("sender", "reciever", "parent_message")
            .prefetch_related("replies")
            .order_by("created_at")
        )
        message_threads = [self.build_thread(msg) for msg in messages if msg.parent_message is None]
        return JsonResponse({"threads": message_threads}, status=200)
                       
class UnreadMessagesView
    def get(self, request):
        user = request.User
        user=User.objects.get(id=user.id)
        unread_messages = Message.unread.unread_for_user(user).only('id', 'sender__username', 'content', 'timestamp')
        data =[]
        if unread_messages is None:
            return JsonResponse({"message": "No unread messages"}, status=200)
        else:
            for unread_message in unread_messages:
                data.append({
                    "id": unread_message.id,
                    "sender": unread_message.sender.username,
                    "content": unread_message.content,
                    "timestamp": unread_message.timestamp,
                            })
            return JsonResponse({"unread_messages": data}, status=200)
        
   
