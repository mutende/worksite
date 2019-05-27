from django.urls import path,include
from authentication.views import ClientSignUpView,FreelancerSignUpView
from authentication import views

urlpatterns = [
    path('client/',include('client.urls')),
    path('freelancer/',include('freelancer.urls')),
    path('signup/client/',ClientSignUpView.as_view(), name='client_signup'),
    path('signup/freelancer/',FreelancerSignUpView.as_view(), name='freelancer_signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
]
