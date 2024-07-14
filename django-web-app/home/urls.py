from django.contrib import admin
from django.urls import path,include
from home import views

from django.views.generic import RedirectView
from home.views import ResetPasswordView

app_name="home"

urlpatterns = [
    path("", views.index, name="home"),
    path("faqs/", views.faqs, name="faqs"),
    path("report-dp/", views.reportDp, name="report-dp"),
    path("about/", views.about, name="about"),
    path("terms-conditions/", views.termsConditions, name="terms-conditions"),
    path("know-about-dp/", views.knowAboutDp, name="know-about-dp"),
    path("login/", views.loginUser, name="loginUser"),
    path("register/", views.registerUser, name="registerUser"),
    path("detected-dp/", views.detected_dp, name="detected-dp"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("verify-email/", views.verifyEmail, name="verify-email"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('health-check/', views.health_check, name='health_check'),
    path('privacy-policy/', views.privacyPolicy, name='privacy-policy'),
    path('terms-of-use/', views.termsOfUse, name='terms-of-use'),
    path('generate-token/', views.generate_token, name='generate_token'),
    path('create-api-key/', views.create_api_key, name='create_api_key'),
    path('delete-api-key/<int:key_id>/', views.delete_api_key, name='delete_api_key'),

    
]



