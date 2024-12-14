from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    # Chats
    path('api/canales/chats/', views.chats_list, name='chats-list'),
    path('api/canales/chats/<int:pk>/', views.chat_detail, name='chat-detail'),

    # Mensajes
    path('api/canales/mensajes/', views.mensajes_list, name='mensajes-list'),
    path('api/chats/<int:chat_id>/mensajes/', views.mensajes_by_chat, name='mensajes-by-chat'),
    path('api/chats/<int:chat_id>/mensajes/<str:username>/', views.mensajes_by_chat_and_user, name='mensajes-by-chat-and-user'),
]