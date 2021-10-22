from django.urls import path

from leave_message import views

app_name = 'message'

urlpatterns = [
    path('leave-massage/', views.leave_message, name='leave_message'),
]