from client.views import ClientHome
from django.urls import path
from client import views
# from client.views import POST_TASK
urlpatterns = [
    path('',ClientHome.as_view(),name="client_home"),
    path('profile/', views.client_profile, name="client_profile"),
    path('change_password/', views.clientChangePassword, name="client_change_password"),
    path('post_task/', views.post_task_view, name="post_task"),
    path('pay/task/<task_id>/', views.pay_for_task, name="pay_for_task"),
    path('confirm/pay/task/<pk>/', views.confirm_payment,name="confirm_payment"),
    path('comment/',views.make_a_comment, name='client_comment'),
    path('task/history/', views.get_my_tasks, name='client_task_history'),
    path('task/bids', views.task_bids, name='view_bids'),
    path('task/assign/<bid_id>/task/<task_id>',views.assign_task, name='assign_task'),
    path('task/freelancer/<profile_id>/profile/',views.freelancer_profile ,name='freelancer_profile'),
    path('task/complete', views.completed_tasks, name='complete_tasks'),
    path('task/bid/complete/<bid_id>/<complete_id>/<freelancer_id>/<task_amount>/', views.complete_task_details, name='complete_task_details'),
    path('reassign_task/bid/<bid_id>/freelancer/<freelancer_id>', views.reassign_task, name="reassign"),
    path('reassigned_tasks/', views.reassigned_task, name="reassigned_tasks_client"),
    path('review/reassigned_task/<bid_id>/<the_id>', views.review_reassigned_task, name="review_reassigned_task"),
    path('help/', views.help, name="client_help"),
]
