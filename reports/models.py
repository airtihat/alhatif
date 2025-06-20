from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    REPORT_TYPES = [
        ('bug', 'بلاغ عن خلل'),
        ('feedback', 'ملاحظات'),
        ('feature', 'طلب ميزة'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.get_report_type_display()})"
