from django.contrib import admin
from django.urls import path,include
from home import views

from django.views.generic import RedirectView

urlpatterns = [
    path("", views.index, name="home"),
    path("faqs/", views.faqs, name="faqs"),
    path("report-dp/", views.reportDp, name="report-dp"),
    path("about/", views.about, name="about"),
    path("terms-conditions/", views.termsConditions, name="terms-conditions"),
    path("know-dp/", views.knowDp, name="knowDp"),
    path("detected_dp/", views.detected_dp, name="detected_dp"),
    
]



