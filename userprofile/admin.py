from django.contrib import admin

# from .models import UserProfile
#
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('student_id', 'username', 'password', 'email', 'name', 'sex', 'qq')
#     list_filter = ('qq', 'created_time')
#     search_fields = ('username', 'name', 'qq')
#     fieldsets = (
#         (None, {
#             'fields': (
#                 ('student_id', 'username',),
#                 ('email', 'password'),
#                 ('name', 'sex', 'qq'),
#             )
#         }),
#     )
#
#
# admin.site.register(UserProfile, UserAdmin)