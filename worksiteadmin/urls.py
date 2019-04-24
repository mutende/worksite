
from django.urls import path
from worksiteadmin import views;

urlpatterns = [
    path('',views.landingpage,name="welcome")
]
