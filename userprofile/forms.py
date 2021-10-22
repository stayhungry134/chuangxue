from django import forms
import re

from django.core.exceptions import ValidationError

from .models import UserProfile


# 登录表单
class LoginForm(forms.Form):
    student_id = forms.CharField(min_length=6)
    password = forms.CharField(min_length=6)


# 注册表单
class RegisterForm(forms.Form):
    student_id = forms.CharField(min_length=13, required=True, error_messages={
        'required': '学号必须输入！',
        'min_length': '学号不符合规范！'
    })
    username = forms.CharField(min_length=3, required=True, error_messages={
        'required': '用户名必须输入！',
        'min_length': '用户名至少3位字符！'
    })
    password = forms.CharField(min_length=6, required=True, error_messages={
        'required': '密码必须输入！',
        'min_length': '密码至少6位字符！'
    })
    re_password = forms.CharField(min_length=6, required=True, error_messages={
        'required': '密码必须输入！',
        'min_length': '密码至少6位字符！'
    })
    email = forms.EmailField(required=True, error_messages={
        'required': '用户名必须输入！',
        'invalid': '邮箱格式不正确！'
    })
    invitation_code = forms.CharField(required=True, error_messages={
        'required': '邀请码必须输入！'
    })

    # 验证两次密码是否一致
    def clean(self):
        password = self.cleaned_data.get('password', None)
        re_password = self.cleaned_data.get('re_password', '')
        if re_password != password:
            raise ValidationError({'re_password': "两次输入的密码不一致！"})
        else:
            return self.cleaned_data

    # 验证学号
    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id', None)
        if re.match(r'^\d{2}43207000\d{3}$', str(student_id)):
            return student_id
        else:
            raise ValidationError("学号不符合规范")

    # 验证邀请码
    def clean_invitation_code(self):
        invitation_code = self.cleaned_data.get('invitation_code', None)
        if str(invitation_code) == 'cxt2020':
            return invitation_code
        else:
            raise ValidationError("邀请码不正确，请联系管理员取得正确的邀请码！")


# 找回密码表单
class RetrieveForm(forms.Form):
    student_id = forms.CharField(min_length=13, required=True, error_messages={
        'required': '学号必须输入！',
        'min_length': '学号不符合规范！'
    })
    email = forms.EmailField(required=True, error_messages={
        'required': '用户名必须输入！',
        'invalid': '邮箱格式不正确！'
    })
    password = forms.CharField(min_length=6, required=True, error_messages={
        'required': '密码必须输入！',
        'min_length': '密码至少6位字符！'
    })
    re_password = forms.CharField(min_length=6, required=True, error_messages={
        'required': '密码必须输入！',
    })

    # 验证两次密码是否一致
    def clean_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if re_password == password:
            return password
        else:
            raise ValidationError({'re_password': "两次输入的密码不一致！"})


