from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm  # ✅ حذف LoginForm لأنه غير موجود
from django.contrib.auth.forms import AuthenticationForm  # ✅ استيراد النموذج الرسمي
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html')  # ✅ إصلاح المسار والإزاحة


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'core/profile.html')
