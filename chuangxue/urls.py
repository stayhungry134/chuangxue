"""chaungxue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 引入用户信息导航，用于登录
    path('', include('userprofile.urls', namespace='userprofile')),
    # 引入文章界面
    path('article/', include('article.urls', namespace='article')),
    # 引入活动界面
    path('schedule/', include('schedule.urls', namespace='schedule')),
    # 引入作品页面
    path('work/', include('work_show.urls', namespace='work')),
    # 引入留言页面
    path('message/', include('leave_message.urls', namespace='message')),
    # 富文本编辑器
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
