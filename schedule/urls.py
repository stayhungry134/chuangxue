from django.urls import path

from schedule import views

app_name = 'schedule'

urlpatterns = [
    # 活动列表
    path('schedule-list/', views.schedule_list, name='schedule_list'),
    # 活动详情
    path('schedule-detail/<int:id>/', views.schedule_detail, name='schedule_detail'),
    # 发布活动
    path('create-schedule/', views.cre_schedule, name='create_schedule'),
]