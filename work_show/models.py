from django.db import models

from userprofile.models import UserProfile


class WorkShow(models.Model):
    # 作品标签
    WORK_ITEMS = [
        (1, 'Python'),
        (2, 'Java'),
        (3, '其他编程'),
        (4, '摄影'),
        (5, '3D打印'),
        (6, '激光雕刻'),
        (0, '其他'),
    ]
    # 作者，参数 on_delete 用于指定数据删除的方式
    work_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='student_id', verbose_name='创作者')
    # 标题
    work_title = models.CharField(max_length=128, verbose_name='作品标题')
    # 内容简介，对作品进行描述的文字
    work_description = models.TextField(verbose_name='作品简介')
    # 作品发布时间，默认写入当前时间
    work_created_time = models.DateTimeField(auto_now_add=True, verbose_name='作品发布时间')
    # 作品图片，可为空
    work_img = models.ImageField(upload_to='work_show/{}/'.format(work_author), blank=True, verbose_name='作品图片')
    # 作品标签
    work_label = models.IntegerField(choices=WORK_ITEMS, verbose_name='作品标签')

    class Meta:
        db_table = 'work_show'  # 表名称
        ordering = ('-work_created_time',)  # 根据 作品创建时间 倒序排列

    def __str__(self):
        return self.work_title
