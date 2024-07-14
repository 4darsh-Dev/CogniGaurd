from django.urls import path
from .views import GenerateTokenView, AnalyzeURLView, TaskStatusView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate-token/', GenerateTokenView.as_view(), name='generate_token'),
    path('analyze-url/', AnalyzeURLView.as_view(), name='analyze_url'),
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),
]