from django.urls import path

from article import views

app_name = 'article'

urlpatterns = [
    # 文章列表
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 发表文章
    path('article-creat/', views.article_creat, name='article_creat'),
    # 编辑文章
    path('article-edit/<int:id>/', views.article_edit, name='article_edit')
]