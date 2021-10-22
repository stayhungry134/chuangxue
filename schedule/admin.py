from django.contrib import admin

from schedule.models import ScheduleList


@admin.register(ScheduleList)
class ScheduleListAdmin(admin.ModelAdmin):
    list_display = ('act_sponsor', 'act_title', 'act_details', 'act_created_time', 'act_time', 'act_img')
    list_filter = ('act_sponsor', 'act_title', )
    search_fields = ('art_sponsor', 'act_title')
    fieldsets = (
        ('活动信息', {
            'fields': (
                ('act_time', 'act_sponsor'),
            )
        }),
        ('活动内容', {
            'fields': (
                ('act_title', 'act_details')
            )
        }),
        ('活动图片', {
            'fields': ('act_img',)
        })
    )
