from django.urls import path
from . import views

urlpatterns = [
    path('', views.ads_list, name='ads_list'),             # ✅ عرض جميع الإعلانات
    path('create/', views.create_ad, name='create_ad'),    # ✅ إنشاء إعلان جديد
]
