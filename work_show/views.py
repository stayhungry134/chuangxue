import markdown
from django.shortcuts import render, redirect

from mytools.login_validation import login_validation
from userprofile.models import UserProfile
from work_show.models import WorkShow


def work_list(request):
    work_selected = 'selected'
    # 取出作品列表
    works = WorkShow.objects.all()[:5]
    return render(request, 'work_show/work_list.html', locals())


def work_detail(request, id):
    work_selected = 'selected'
    # 取出作品
    work = WorkShow.objects.get(id=id)
    work.work_description = markdown.markdown(work.work_description, extensions=[
        # 包含 缩写、表格等常用扩展
        'extra', 'toc',
        # 语法高亮扩展
        'codehilite',
        'toc'
    ])
    return render(request, 'work_show/work_detail.html', locals())


# 创建作品
@login_validation
def cre_work(request):
    work_labels = WorkShow.WORK_ITEMS
    work_label = 0
    if request.method == 'POST':
        data = request.POST
        for label in work_labels:
            if data['work_label'] == label[1]:
                work_label = label[0]
        WorkShow.objects.create(
            work_author=UserProfile.objects.get(student_id=request.session['student_id']),
            work_title=data['work_title'],
            work_description=data['work_body'],
            work_label=work_label
        )
        return redirect('work:work_list')
    return render(request, 'work_show/work_create.html', locals())


# 编辑作品
def work_edit(request, id):
    work = WorkShow.objects.get(id=id)
    work_label = WorkShow.WORK_ITEMS[work.work_label][1]
    if request.method == 'POST':
        data = request.POST
        if data['work_title'] == '':
            work.work_description = data['work_body']
            work.save()
        else:
            work.work_title = data['work_title']
            work.work_description = data['work_body']
            work .save()
        return redirect('work:work_detail', id=id)
    return render(request, 'work_show/work_edit.html', locals())