from django.shortcuts import render,redirect
from django.http import JsonResponse
# Create your views here.
from .models import WebsiteTransparencyScore

def tpScore(request):
    tScore = transparencyCalc(request)
    return JsonResponse({"transparency_score": tScore})

def transparencyCalc(request):
    tScore = 8.5

    # Save the transparency score to the database
    website_name = "example.com"  # Replace with the actual website name
    WebsiteTransparencyScore.objects.update_or_create(
        website_name=website_name,
        defaults={'transparency_score': tScore}
    )

    return tScore
