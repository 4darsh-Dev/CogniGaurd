from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("tp-score/", views.tpScore, name="tpScore"),
    path("dp-data/", views.dpData, name="dpData"),
    
]
