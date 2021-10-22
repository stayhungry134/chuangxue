from django.urls import path

from work_show import views

app_name = 'work'

urlpatterns = [
    # 作品列表
    path('work-list/', views.work_list, name='work_list'),
    # 作品详情
    path('work-detail/<int:id>/', views.work_detail, name='work_detail'),
    # 发布作品
    path('cre_work/', views.cre_work, name='cre_work'),
    # 编辑作品
    path('work-edit/<int:id>/', views.work_edit, name='work_edit'),
]