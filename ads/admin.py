from django.contrib import admin
from .models import AdCampaign

@admin.register(AdCampaign)
class AdCampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'campaign_type', 'status', 'user', 'created_at')
    list_filter = ('campaign_type', 'status', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
