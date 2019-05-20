from client.views import ClientHome
from django.urls import path
from client import views
from client.views import POST_TASK
urlpatterns = [
    path('',ClientHome.as_view(),name="client_home"),
    path('login/',views.loginClient, name="login_client"),
    path('logout/', views.logoutClient, name="logout_client"),
    path('profile/', views.client_profile, name="client_profile"),
    path('change_password/', views.clientChangePassword, name="client_change_password"),
    path('post_task/', views.post_task_view, name="post_task"),
    path('comment/',views.make_a_comment, name='client_comment'),
]
