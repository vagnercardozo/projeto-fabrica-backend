# core/admin.py
from django.contrib import admin
from .models import Projeto, Status

admin.site.register(Projeto)
admin.site.register(Status)