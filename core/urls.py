from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # ✅ استيراد views الخاصة بالمصادقة

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),  # http://127.0.0.1:8000/profile/
    path('register/', views.register_view, name='register'),  # ✅ صفحة التسجيل
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]
