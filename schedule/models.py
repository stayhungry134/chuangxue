from django.db import models

from userprofile.models import UserProfile


class ScheduleList(models.Model):
    # 活动发起人
    act_sponsor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='student_id', verbose_name='发起人')
    # 活动标题
    act_title = models.CharField(max_length=128, verbose_name='活动标题')
    # 活动内容
    act_details = models.TextField(verbose_name='活动详情')
    # 活动发起时间
    act_created_time = models.DateTimeField(auto_now_add=True, verbose_name='活动发起时间')
    # 活动时间
    act_time = models.DateTimeField(verbose_name='活动时间')
    # 活动图片，可为空
    act_img = models.ImageField(upload_to='schedule/%Y%m/', verbose_name='活动图片', blank=True)

    class Meta:
        db_table = 'schedule'  # 表名称
        ordering = ('-id',)  # 根据 活动时间 倒序排列

    def __str__(self):
        return self.act_title
