from django.db import models
from django.utils import timezone

from userprofile.models import UserProfile


class Article(models.Model):
    ARTICLE_ITEMS = [
        (0, '未分组'),
        (1, 'Python'),
        (2, '计算机/编程'),
        (3, '摄影'),
        (4, '其他技术类'),
        (5, '随笔'),
        (6, '其他'),
    ]
    # 作者，参数 on_delete 用于指定数据删除的方式
    art_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='student_id', verbose_name='文章作者')
    # 文章标题
    art_title = models.CharField(max_length=128, verbose_name='文章标题')
    # 文章正文，保存大量文本
    art_body = models.TextField(verbose_name='文章正文', help_text="建议使用 markdown 语法")
    # 文章创建时间，默认写入当前时间
    art_created_time = models.DateTimeField(default=timezone.now, verbose_name='文章创建时间')
    # 文章更新时间，每次数据更新时自动写入当前时间
    art_updated_time = models.DateTimeField(auto_now=True, verbose_name='上一次编辑时间')
    # 文章中的图片， 可为空
    article_img = models.ImageField(upload_to='article/{}/'.format(art_author), blank=True, verbose_name='文章图片')
    # 文章标签
    article_label = models.IntegerField(choices=ARTICLE_ITEMS, verbose_name='文章标签')

    class Meta:
        db_table = 'article'  # 表名称
        ordering = ('-id',)  # 根据 创建时间 倒序排列

    def __str__(self):
        return self.art_title
