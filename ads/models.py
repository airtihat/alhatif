from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AdCampaign(models.Model):
    CAMPAIGN_TYPES = [
        ('internal', 'داخلي فقط'),
        ('google', 'Google Ads'),
        ('facebook', 'Meta (Facebook/Instagram)'),
        ('tiktok', 'TikTok Ads'),
        ('combined', 'متكامل'),
    ]

    STATUS_CHOICES = [
        ('draft', 'مسودة'),
        ('active', 'نشط'),
        ('paused', 'متوقف'),
        ('completed', 'مكتمل'),
    ]

    # ✅ تم السماح بـ null مؤقتًا لتفادي خطأ الترحيل
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ad_campaigns', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    campaign_type = models.CharField(max_length=20, choices=CAMPAIGN_TYPES, default='internal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
