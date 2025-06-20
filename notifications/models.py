from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    CHANNEL_CHOICES = [
        ('email', 'البريد الإلكتروني'),
        ('sms', 'رسالة نصية'),
        ('whatsapp', 'واتساب'),
    ]

    # المستلم: ارتباط بنموذج المستخدم
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name="المستلم")
    
    # الرسالة: النص المرسل في الإشعار
    message = models.TextField(verbose_name="محتوى الإشعار")
    
    # القناة: لتحديد كيفية إرسال الإشعار
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES, default='email', verbose_name="طريقة الإرسال")
    
    # تاريخ الإرسال: يتم تحديده تلقائيًا عند الإنشاء
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    def __str__(self):
        return f"إشعار إلى {self.recipient.username} عبر {self.get_channel_display()}"

    class Meta:
        verbose_name = "إشعار"
        verbose_name_plural = "الإشعارات"
        ordering = ['-created_at']  # ترتيب الإشعارات حسب تاريخ الإنشاء بشكل تنازلي
