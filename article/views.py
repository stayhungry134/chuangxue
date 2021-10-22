import markdown
from django.shortcuts import render, redirect

from article.models import Article

from mytools.login_validation import login_validation

# 文章列表
from userprofile.models import UserProfile


def article_list(request):
    article_selected = 'selected'
    articles = Article.objects.all()
    return render(request, 'article/article_list.html', locals())


# 文章详情
def article_detail(request, id):
    article_selected = 'selected'
    # 取出对应文章
    article = Article.objects.get(id=id)
    # 使用Markdown语法渲染
    article.art_body = markdown.markdown(article.art_body, extensions=[
        # 包含 缩写、表格等常用扩展
        'extra', 'toc',
        # 语法高亮扩展
        'codehilite',
        'toc'
    ])
    return render(request, 'article/article_detail.html', locals())


# 发表文章
@login_validation
def article_creat(request):
    article_labels = Article.ARTICLE_ITEMS
    article_label = 0
    if request.method == 'POST':
        data = request.POST
        for label in article_labels:
            if data['article_label'] == label[1]:
                article_label = label[0]
        Article.objects.create(
            art_author=UserProfile.objects.get(student_id=request.session['student_id']),
            art_title=data['art_title'],
            art_body=data['art_body'],
            article_label=article_label
        )
        return redirect('article:article_list')
    return render(request, 'article/article_creat.html', locals())


# 编辑文章
def article_edit(request, id):
    article = Article.objects.get(id=id)
    art_label = Article.ARTICLE_ITEMS[article.article_label][1]
    if request.method == 'POST':
        data = request.POST
        if data['art_title'] == '':
            article.art_body = data['art_body']
            article.save()
        else:
            article.art_title = data['art_title']
            article.art_body = data['art_body']
            article.save()
        return redirect('article:article_detail', id=id)
    return render(request, 'article/article_edit.html', locals())
