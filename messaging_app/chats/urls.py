from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageListView.as_view(), name='messages'),
    path('messages/<uuid:pk>/', views.MessageDetailView.as_view(), name='message-detail'),
    
    path('conversations/', views.ConversationListView.as_view(), name='conversations'),
    path('conversations/<uuid:pk>/', views.ConversationDetailView.as_view(), name='conversation-detail'),
]
