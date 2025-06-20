from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NotificationForm
from .models import Notification
from django.utils import timezone

# ✅ الصفحة الرئيسية: مركز الإشعارات
def notification_index(request):
    return render(request, 'notifications/index.html')

# ✅ عرض قائمة الإشعارات
def notification_list(request):
    notifications = Notification.objects.order_by('-created_at')  # استخدام 'created_at' بدلاً من 'sent_at'
    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications
    })

# ✅ إرسال إشعار جديد
def send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.created_at = timezone.now()  # تعيين التاريخ تلقائيًا
            notification.save()
            messages.success(request, '✅ تم إرسال الإشعار بنجاح')
            return redirect('notifications:notification_list')
    else:
        form = NotificationForm()

    return render(request, 'notifications/notification_form.html', {
        'form': form
    })

# ✅ صفحة إعدادات الإشعارات
def notification_settings(request):
    return render(request, 'notifications/notification_settings.html')
