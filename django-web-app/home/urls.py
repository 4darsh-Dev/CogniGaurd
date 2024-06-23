from django.contrib import admin
from django.urls import path,include
from home import views

from django.views.generic import RedirectView

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
    


    
]



