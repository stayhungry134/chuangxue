from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    # 首页，登录界面
    path('', views.user_login, name='login'),
    # 注册页面
    path('register/', views.user_register, name='register'),
    # 找回密码
    path('retrieve/', views.user_retrieve, name='retrieve'),
    # 用户信息
    path('user_edit/', views.user_edit, name='user_edit'),
    # 创学堂首页
    path('index/', views.index, name='index'),
]