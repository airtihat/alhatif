from django.contrib import admin
from .models import APIRequest

@admin.register(APIRequest)
class APIRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
