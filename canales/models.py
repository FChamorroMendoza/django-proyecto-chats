from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User  # Para usar el modelo User de Django


class Chat(models.Model):
    # Definición del modelo Chat
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    # Definición del modelo Mensaje
    user = models.ForeignKey(User, related_name='mensajes', on_delete=models.CASCADE)  # Relación con User
    chat = models.ForeignKey(Chat, related_name='mensajes', on_delete=models.CASCADE)  # Relación con Chat
    contenido = models.CharField(max_length=300)
    creado = models.DateTimeField(auto_now_add=True)  # Este campo se asigna automáticamente

    def __str__(self):
        return f"Mensaje de {self.user.username} en {self.chat.nombre}"

    
    
    
    
    

