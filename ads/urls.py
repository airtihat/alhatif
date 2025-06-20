from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.ad_list, name='ad_list'),            # قائمة الإعلانات
    path('create/', views.create_ad, name='create_ad'), # إنشاء إعلان
]
