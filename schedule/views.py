import markdown
from django.shortcuts import render, redirect

from schedule.models import ScheduleList


# 活动列表
from userprofile.models import UserProfile


def schedule_list(request):
    schedule_selected = 'selected'
    # 取出活动
    schedules = ScheduleList.objects.all()
    return render(request, 'schedule/schedule_list.html', locals())


# 活动详情
def schedule_detail(request, id):
    schedule_selected = 'selected'
    schedule = ScheduleList.objects.get(id=id)
    schedule.act_details = markdown.markdown(schedule.act_details, extensions=[
        # 包含 缩写、表格等常用扩展
        'extra', 'toc',
        # 语法高亮扩展
        'codehilite',
        'toc'
    ])
    return render(request, 'schedule/schedule_detail.html', locals())


def cre_schedule(request):
    if request.method == 'POST':
        data = request.POST
        ScheduleList.objects.create(
            act_sponsor=UserProfile.objects.get(student_id=request.session['student_id']),
            act_time=data['act_date'] + 'T' + data['act_time'],
            act_details=data['act_detail'],
            act_title=data['act_title'],
        )
        return redirect('schedule:schedule_list')
    return render(request, 'schedule/schedule_create.html', locals())
