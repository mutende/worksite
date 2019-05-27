from client.views import ClientHome
from django.urls import path
from client import views
# from client.views import POST_TASK
urlpatterns = [
    path('',ClientHome.as_view(),name="client_home"),
    path('profile/', views.client_profile, name="client_profile"),
    path('change_password/', views.clientChangePassword, name="client_change_password"),
    path('post_task/', views.post_task_view, name="post_task"),
    path('comment/',views.make_a_comment, name='client_comment'),
    path('task/history/', views.get_my_tasks, name='client_task_history'),
    path('task/bids', views.task_bids, name='view_bids'),
    path('task/assign/<bid_id>/task/<task_id>',views.assign_task, name='assign_task'),
    path('task/freelancer/<profile_id>/profile/',views.freelancer_profile ,name='freelancer_profile')
]
