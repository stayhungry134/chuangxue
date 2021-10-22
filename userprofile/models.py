from django.db import models


# Create your models here.
class UserProfile(models.Model):
    SEX_ITEMS = [
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    ]
    # 学号，主键，用于登录
    student_id = models.CharField(primary_key=True, max_length=32, verbose_name='学号')
    # 用户名，发表文章显示的字段
    username = models.CharField(max_length=64, verbose_name='用户名')
    # 密码
    password = models.CharField(max_length=128, verbose_name='密码')
    # 邮箱，用于找回密码或者验证
    email = models.EmailField(verbose_name='Email')
    # 姓名，便于内部管理，可为空
    name = models.CharField(max_length=32, verbose_name='姓名', blank=True)
    # 性别
    sex = models.IntegerField(choices=SEX_ITEMS, default=0, verbose_name='性别')
    # QQ号，可为空
    qq = models.CharField(max_length=32, verbose_name='QQ', blank=True)
    # 注册时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    # 用户头像，可为空
    user_img = models.ImageField(upload_to='userprofile/', verbose_name='用户头像', blank=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
