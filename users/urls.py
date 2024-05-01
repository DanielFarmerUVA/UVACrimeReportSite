from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path("report", views.report, name = "report"),
    path("success", views.report_upload, name = "submit"),
    path('anon-home/', views.anon_home, name='anon_home'),  # anon login
    path("anon-home/logout", views.logout_view),
    path('admin-home/', views.admin_home, name='admin_home'),  # admin home page

    path('user-home/', views.user_home, name='user-home'), 
    path('admin-report-detail/<int:report_id>/', views.admin_report_detail, name='admin_report_detail'),     # Path for admin users to view reports
    path('user-report-detail/<int:report_id>/', views.user_report_detail, name='user_report_detail'),     # Path for regular users to view their submissions
]