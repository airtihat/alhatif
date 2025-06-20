from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('subject', 'report_type', 'user', 'submitted_at')
    search_fields = ('subject', 'description')
    list_filter = ('report_type', 'submitted_at')
