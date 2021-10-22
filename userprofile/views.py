from django.shortcuts import render, redirect
import hashlib

from article.models import Article
from mytools.login_validation import login_validation
from schedule.models import ScheduleList
from userprofile.forms import LoginForm, RegisterForm
from userprofile.models import UserProfile


# 加密密码
from work_show.models import WorkShow


def hash_code(s, salt='cxt2020nb'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update 方法只接收 bytes 类型
    return h.hexdigest()


# 登录页面
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            student_id = login_form.cleaned_data.get('student_id')
            password = login_form.cleaned_data.get('password')
            try:
                user = UserProfile.objects.get(student_id=student_id)
                if user.password == hash_code(password):
                    # 将用户数据储存在 session 中
                    request.session['student_id'] = user.student_id
                    request.session['username'] = user.username
                    return redirect('userprofile:index')
                else:
                    password_error = "密码不正确"
                    return render(request, 'userprofile/login.html', locals())
            except:
                student_id_error = "此用户不存在"
                return render(request, 'userprofile/login.html', locals())
    return render(request, 'userprofile/login.html')


# 注册页面
def user_register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            # 学号唯一
            student_id = UserProfile.objects.filter(student_id=data['student_id'])
            if student_id:
                student_id_error = "此学号已被注册"
                return render(request, 'userprofile/register.html', locals())
            # 用户名唯一
            username = UserProfile.objects.filter(username=data['username'])
            if username:
                username_error = "此用户名以被注册，请更换用户名"
                return render(request, 'userprofile/register.html', locals())
            # 邮箱唯一
            email = UserProfile.objects.filter(email=data['email'])
            if email:
                email_error = "此邮箱已被注册，请更换邮箱"
                return render(request, 'userprofile/register.html', locals())
            # 加密密码
            data['password'] = hash_code(data['password'])
            # 删除多余数据
            data.pop('re_password')
            data.pop('invitation_code')
            # 存储数据
            UserProfile.objects.create(**data)
            return redirect('userprofile:login')
        else:
            return render(request, 'userprofile/register.html', {'form': register_form})
    return render(request, 'userprofile/register.html')


# 找回密码页面
def user_retrieve(request):
    return render(request, 'userprofile/retrieve.html')


# 创学堂首页
def index(request):
    index_selected = 'selected'
    articles = Article.objects.all()[:5]
    works = WorkShow.objects.all()[:5]
    schedules = ScheduleList.objects.all()[:5]
    return render(request, 'userprofile/index.html', locals())


@login_validation
def user_edit(request):
    user = UserProfile.objects.get(student_id=request.session['student_id'])
    sex_items = UserProfile.SEX_ITEMS
    sex = user.sex
    user_sex = sex_items[sex][1]
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        for item in sex_items:
            if data['sex'] == item[1]:
                sex = item[0]
        qq = data['qq']
        user_img = request.FILES.get('user_img')
        if name != '':
            user.name = name
        user.sex = sex
        if qq != '':
            user.qq = qq
        # if user_img != '':
        #     user.user_img = user_img
        user.save()
        return redirect('userprofile:user_edit')
    return render(request, 'userprofile/user_pro.html', locals())