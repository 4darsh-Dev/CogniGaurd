from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def faqs(request):
    return render(request, "faqs.html")

def popup_detect(request):
    pass