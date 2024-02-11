from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("faqs/", views.faqs, name="faqs"),
    path("report-dp/", views.reportDp, name="report-dp"),
    path("about/", views.about, name="about"),
    path("terms-conditions/", views.termsConditions, name="terms-conditions"),
    path("know-dp/", views.knowDp, name="knowDp"),

]



