from django.shortcuts import render
from django.http import HttpResponse
from .models import Message, MessageHistory, User


class DeleteUser:
    def post(self, request, user_id):
        user = request.user
        if user.id != user_id:
            return HttpResponse("Unauthorized", status=401)
        try:
            user_to_delete = User.objects.get(id=user_id)
            user_to_delete.delete()
            return HttpResponse("User and related data deleted successfully", status=200)
        except User.DoesNotExist:
            return HttpResponse("User not found", status=404)
        
        
# Create your views here.
