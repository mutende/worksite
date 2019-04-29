
from django.urls import path
from client import views
urlpatterns = [
    path('',views.clientHome,name="client_home"),
]
