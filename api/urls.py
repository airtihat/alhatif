from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('create/', views.create_request, name='create_request'),
]
