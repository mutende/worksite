
from django.urls import path
from django.conf.urls import url
from freelancer.views import TaskDetails,ViewTask
from freelancer import views

urlpatterns = [
    # path('', FreelancerHome.as_view(),name="freelancer_home"),
    path('',views.freelancer_home, name="freelancer_home"),  
    path('profile/', views.freelancer_profile, name="freelancer_profile"),
    path('change_password/', views.freelancerChangePassword, name="freelancer_change_password"),
    url(r'^tasks/', ViewTask.as_view(), name="view_tasks"),
    url(r'^task/view/(?P<pk>[0-9]+)/$', TaskDetails.as_view(), name="task_details"),
    path('comment/', views.make_a_comment ,name="freelancer_comment"),
    url(r'^task/bid/(?P<task_id>[0-9]+)/$', views.make_a_bid, name="place_bid"),
    path('assigned/', views.get_assigned_tasks, name="assigned"),
    path('submit/task/bid/<bid_id>/', views.submit_a_task, name="submit_task"),
    path('reassigned/', views.get_reassigned_task, name="reassigned_tasks"),
    path('submit/reassigned/<id>/', views.submit_reassigned_task, name="submit_reassigned_tasks"),
    path('help/', views.help, name="help"),
    
]
