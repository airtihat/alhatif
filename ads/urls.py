from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('create/', views.create_ad, name='create_ad'),
]
