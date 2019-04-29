
from django.urls import path
from freelancer import views

urlpatterns = [
    path('',views.freelancerHome,name="freelancer_home"),
]
