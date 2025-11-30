from rest_framework.permissions import BasePermission, IsAuthenticated

class IsParticipantOfConversation(BasePermission):
    """
    Allows access only to authenticated users who are participants
    in the conversation linked to the message/conversation.
    """

    message = "You must be a participant in this conversation."

    def has_permission(self, request, view):
        # Require authentication first
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        obj can be:
        - Message: check obj.conversation.participants
        - Conversation: check obj.participants
        """

        # If object is a Conversation
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()

        # If object is a Message
        if hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()

        return False
