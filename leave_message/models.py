from django.db import models

from userprofile.models import UserProfile


class MessageList(models.Model):
    # 留言用户
    msg_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='student_id', verbose_name='留言用户')
    # 留言时间
    msg_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    # 留言内容
    msg_body = models.TextField(verbose_name='留言内容')

    class Meta:
        db_table = 'message_list'  # 表名称
        ordering = ('-id',)  # 根据 留言时间 倒序排列
