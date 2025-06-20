from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_home, name='report_home'),  # الآن /reports/ تشتغل
    path('submit/', views.submit_report, name='submit_report'),
    path('<int:report_id>/', views.report_detail, name='report_detail'),
    path('<int:report_id>/download/', views.report_download, name='report_download'),
]
