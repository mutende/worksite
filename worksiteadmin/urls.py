
from django.urls import path,include
from worksiteadmin.views import WorksiteAdminHome

urlpatterns = [
    path('',WorksiteAdminHome.as_view(),name="welcome"),
    path('client/',include('client.urls')),
    path('freelancer/',include('freelancer.urls')),
    path('',include('authentication.urls')),
]
