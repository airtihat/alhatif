from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    CHANNEL_CHOICES = [
        ('email', 'البريد الإلكتروني'),
        ('sms', 'رسالة نصية'),
        ('whatsapp', 'واتساب'),
    ]

    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"إشعار إلى {self.recipient.username} عبر {self.channel}"
