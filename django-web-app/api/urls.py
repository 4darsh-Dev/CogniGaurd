from django.urls import path
from . import views

urlpatterns = [
    path('analyze-url/', views.AnalyzeURLView.as_view(), name='analyze-url'),
    path('task-status/<str:task_id>/', views.TaskStatusView.as_view(), name='task-status'),
    path('dp-request-list/', views.MessageListView.as_view(), name='dp-request-list'),
]