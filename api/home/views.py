from django.shortcuts import render,redirect
from .popup_detect_ml import predict
from django.http import JsonResponse
from json import dump

# Create your views here.

def index(request):
    return render(request, "index.html")

def faqs(request):
    return render(request, "faqs.html")

def popup_detect(request):
    img = request.GET.get('img', '')
    return JsonResponse(dump(predict(img)))
    