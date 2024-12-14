from django.contrib import admin

# Register your models here.

# canales/admin.py
from .models import Chat, Mensaje

admin.site.register(Chat)
admin.site.register(Mensaje)

