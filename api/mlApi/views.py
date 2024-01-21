from django.shortcuts import render,redirect
from django.http import JsonResponse

# Create your views here.
from .models import WebsiteTransparencyScore

import sys
sys.path.append("F:\backup-kali\codeFiles\projects\cognigaurd\api\scraping")
from 

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

def dpData(request):

    # Extract the URL from the request
    url = request.GET.get('url', '')

    # Call the scraping function and get the text
    
    scraped_text = scrape_text_from_url(url)

    # Fine-tune BERT model and classify dark pattern
    predicted_label = fine_tune_and_classify(scraped_text)

    # Save the result in the SQLite3 database
    website = Website.objects.get_or_create(url=url)[0]
    dark_pattern = DarkPattern.objects.create(website=website, label=predicted_label)

    return JsonResponse({"dp_data": "This is the dark pattern data"})