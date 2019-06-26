
from django.urls import path,include
from worksiteadmin.views import WorksiteAdminHome
from worksiteadmin import views


urlpatterns = [
    path('',WorksiteAdminHome.as_view(),name="welcome"),
    path('client/',include('client.urls')),
    path('freelancer/',include('freelancer.urls')),
    path('',include('authentication.urls')),
    path('admin/reports/', views.report_home, name="report_home"),
    path('admin/help/', views.admin_help, name="admin_help"),
    path('admin/freelancers-report/', views.freelancers_report, name="freelancers_report"),
    path('admin/bids-report/', views.bids_report, name="bids_report"),
    path('admin/payment-report/', views.payments_summery_report, name="payments_summery"),
    path('admin/clients-report/', views.clients_report, name="clients_report"),
    path('admin/task-report/', views.tasks_report, name="tasks_report"),
    path('admin/reassigned-tasks-report/', views.reassigned_tasks_report, name="reassigned_tasks_report"),
     path('admin/task-payment-report/', views.mpesa_payments_report, name="task_payment_report"),
    
]
