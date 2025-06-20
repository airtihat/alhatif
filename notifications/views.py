from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NotificationForm

def send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال الإشعار بنجاح ✅')
            return redirect('notifications:send_notification')
    else:
        form = NotificationForm()
    return render(request, 'notifications/notification_form.html', {'form': form})
