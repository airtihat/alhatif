from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  


# ✅ التسجيل
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # إرسال رسالة ترحيب
            subject = '🎉 مرحبًا بك في دليل الهاتف'
            message = render_to_string('emails/welcome_email.html', {'user': user})
            send_mail(
                subject,
                '',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=message,
                fail_silently=False,
            )

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/register.html', {'form': form})


# ✅ تسجيل الدخول
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


# ✅ الملف الشخصي
@login_required
def profile_view(request):
    return render(request, 'core/profile.html')

def register_view(request):
    return render(request, 'core/register.html')