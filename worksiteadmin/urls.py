
from django.urls import path,include
from worksiteadmin import views

urlpatterns = [
    path('',views.landingpage,name="welcome"),
    path('client/',include('client.urls')),
    path('freelancer/',include('freelancer.urls')),
]
