from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path,include
>>>>>>> 7fb99d1719b011518f106d67414c183667809f90
from . import views
# from mlApi.views import csrf_view

urlpatterns = [
    path("tp-score/", views.tpScore, name="tpScore"),
<<<<<<< HEAD
    # path("dp-data/", views.dpData, name="dpData"),

    # Implmentaion for the DRF views
    path('dp-request/', views.MessageCreateView.as_view(), name='dp-request'),
    path('dp-request-list/', views.MessageListView.as_view(), name='dp-request-list'),
    
   
=======
    path("dp-data/", views.dpData, name="dpData"),
    # path('api/csrf/', csrf_view, name='csrf_endpoint'),
    path('csrf/', views.csrf_token_view, name='csrf_token_view'),
>>>>>>> 7fb99d1719b011518f106d67414c183667809f90
    
]
