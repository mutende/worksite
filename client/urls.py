from client.views import ClientHome
from django.urls import path
from client import views
urlpatterns = [
    path('',ClientHome.as_view(),name="client_home"),
    path('login/',views.loginClient, name="login_client"),
    path('logout/', views.logoutClient, name="logout_client"),
    path('profile/', views.client_profile, name="client_profile"),
    path('change_password/', views.clientChangePassword, name="client_change_password"),
]
