
from django.urls import path
from freelancer.views import FreelancerHome
from freelancer import views

urlpatterns = [
    path('', FreelancerHome.as_view(),name="freelancer_home"),
    path('login/',views.loginFreelancer, name="login_freelancer"),
    path('logout/', views.logoutFreelancer, name="logout"),
    path('profile/', views.freelancer_profile, name="freelancer_profile"),
    path('change_password/', views.freelancerChangePassword, name="freelancer_change_password"),
    path('tasks/', views.view_tasks, name="view_tasks"),
]
