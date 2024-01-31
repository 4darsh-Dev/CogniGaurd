from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("faqs/", views.faqs, name="faqs"),
    path("popup_detect/", views.popup_detect, name="popup_detect"),
    path("report-dp/", views.reportDp, name="report-dp"),
    path("about/", views.about, name="about"),
]
