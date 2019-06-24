
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
     path('admin/freelancers-report/', views.generate_freelancers_pdf, name="freelancers_pdf"),
]
