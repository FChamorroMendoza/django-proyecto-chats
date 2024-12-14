from rest_framework import serializers
from .models import Chat, Mensaje
from django.contrib.auth.models import User

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'nombre']

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id', 'user', 'chat', 'contenido', 'creado']
