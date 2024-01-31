from django.contrib import admin
from django.urls import path,include
from . import views
# from mlApi.views import csrf_view

urlpatterns = [
    path("tp-score/", views.tpScore, name="tpScore"),
    path("dp-data/", views.dpData, name="dpData"),
    # path('api/csrf/', csrf_view, name='csrf_endpoint'),
    path('csrf/', views.csrf_token_view, name='csrf_token_view'),
    
]
