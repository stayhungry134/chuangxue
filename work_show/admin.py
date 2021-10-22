from django.contrib import admin

from .models import WorkShow


class WorkShowAdmin(admin.ModelAdmin):
    list_display = ('work_author', 'work_title', 'work_description', 'work_label', 'work_created_time')
    list_filter = ('work_author', 'work_title', 'work_label')
    search_fields = ('work_author', 'work_title')
    fieldsets = (
        ('作品信息', {
           'fields': (
               'work_author', 'work_label'
           )
        }),
        ('作品内容', {
           'fields': (
               ('work_title', 'work_description')
           )
        }),
        ('作品图片', {
            'fields': ('work_img',)
        }),
    )


admin.site.register(WorkShow, WorkShowAdmin)
