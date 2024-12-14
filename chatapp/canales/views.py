from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Mensaje, Chat
from .serializers import ChatSerializer, MensajeSerializer

@api_view(['GET', 'POST'])
def chats_list(request):
    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH'])
def chat_detail(request, pk):
    try:
        chat = Chat.objects.get(pk=pk)
    except Chat.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':  # Añadido manejo para 'PATCH'
        serializer = ChatSerializer(chat, data=request.data, partial=True)  # partial=True permite actualizaciones parciales
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def mensajes_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Número de mensajes por página
        mensajes = Mensaje.objects.all()
        result_page = paginator.paginate_queryset(mensajes, request)
        serializer = MensajeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def mensajes_by_chat(request, chat_id):
    mensajes = Mensaje.objects.filter(chat=chat_id)
    serializer = MensajeSerializer(mensajes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def mensajes_by_chat_and_user(request, chat_id, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    mensajes = Mensaje.objects.filter(chat=chat_id, user=user)
    serializer = MensajeSerializer(mensajes, many=True)
    return Response(serializer.data)
