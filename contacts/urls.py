from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('create/', views.create_contact, name='create_contact'),
]
