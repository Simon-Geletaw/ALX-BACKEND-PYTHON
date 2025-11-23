from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to objects owned by the requesting user.
    """

    def has_object_permission(self, request, view, obj):
        # For messages where sender = message.user
        if hasattr(obj, "user"):
            return obj.user == request.user

        # For conversations where user is a participant
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()

        return False
