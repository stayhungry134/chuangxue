from django.shortcuts import render, redirect

# Create your views here.
from leave_message.models import MessageList
from mytools.login_validation import login_validation
from userprofile.models import UserProfile


@login_validation
def leave_message(request):
    message_selected = 'selected'
    messages = MessageList.objects.all()
    # 如果用户提交留言
    if request.method == 'POST':
        data = request.POST
        MessageList.objects.create(
            msg_user=UserProfile.objects.get(student_id=request.session['student_id']),
            msg_body=data['msg_body']
        )
        return redirect('message:leave_message')
    return render(request, 'save_message/save_message.html', locals())