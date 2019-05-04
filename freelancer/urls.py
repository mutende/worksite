
from django.urls import path
from freelancer.views import FreelancerHome
from freelancer import views

urlpatterns = [
    path('', FreelancerHome.as_view(),name="freelancer_home"),
    path('login/',views.loginFreelancer, name="login_freelancer"),
    path('logout/', views.logoutFreelancer, name="logout"),
]
