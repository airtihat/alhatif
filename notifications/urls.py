from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_index, name='index'),                       # /notifications/
    path('list/', views.notification_list, name='notification_list'),       # /notifications/list/
    path('send/', views.send_notification, name='send_notification'),       # /notifications/send/
    path('settings/', views.notification_settings, name='notification_settings'),  # /notifications/settings/
]
