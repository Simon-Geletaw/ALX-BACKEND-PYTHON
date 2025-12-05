from django.http import HttpResponse, JsonResponse
from .models import Message,  User
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .models import Message,  User
from django.db.models import Q


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
        
        
# Create your views here.
