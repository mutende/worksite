from django.urls import path,include
from authentication.views import ClientSignUpView,FreelancerSignUpView
from authentication import views

urlpatterns = [
    path('client/',include('client.urls')),
    path('freelancer/',include('freelancer.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup/client/',ClientSignUpView.as_view(), name='client_signup'),
    path('signup/freelancer/',FreelancerSignUpView.as_view(), name='freelancer_signup'),
    path('signup/', views.signupview, name='signup'),
    # path('account/activation/', views.client_account, name="client_account_activation"),
]
