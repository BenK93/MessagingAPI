from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Message


admin.site.register(Message)
