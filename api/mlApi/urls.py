from django.contrib import admin
from django.urls import path, include
from . import views
# from mlApi.views import csrf_view

urlpatterns = [
    path("tp-score/", views.tpScore, name="tpScore"),
    # path("dp-data/", views.dpData, name="dpData"),

    # Implmentaion for the DRF views
    path('dp-request/', views.MessageCreateView.as_view(), name='dp-request'),
    path('dp-request-list/', views.MessageListView.as_view(), name='dp-request-list'),
    
   
    
]
