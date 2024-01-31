from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse

# Create your views here.
from .models import WebsiteTransparencyScore, DarkPatternsData

from scraping.dp_scrape import get_scrape_data

from django.middleware.csrf import get_token

# Import the urllib.parse library
from urllib.parse import urlparse


def csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def index(request):
    return HttpResponse("Hello, world. You're at Django API Index.")



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

    print("I am executing! ")
    # Extract the URL from the request
    url = request.GET.get('url', None)
    print(url)

    if url is not None:
        # Remove URL-encoded double quotes ("%22") from the beginning and end
        url = urlparse(url).path

        # Check if the scheme is missing and add a default scheme
        parsed_url = urlparse(url)

        # Remove double quotes from the URL
        url = url.strip('"')

        if not parsed_url.scheme:
            url = url
            newUrl = url
            print(f"Final url {newUrl}")
            
            scraped_text = get_scrape_data(newUrl)

        

            # print(scraped_text) 


        # return "done! succesfully scraping"

        # Fine-tune BERT model and classify dark pattern
        # predicted_labels = fine_tune_and_classify(scraped_text)
        
        predicted_labels= {"dp_data": "This is the dark pattern data"}

        # Save the dark pattern data in the DarkPatternData model
        # website_url = url
        # for label, dark_text in predicted_labels.items():
        #     dark_pattern, created = DarkPatternsData.objects.get_or_create(
        #         website_url=website_url,
        #         dark_pattern_label=label,
        #         defaults={'dark_text': dark_text}
        #     )

        #     # If the record already exists, update the dark_text field
        #     if not created:
        #         dark_pattern.dark_text = dark_text
        #         dark_pattern.save()

    return JsonResponse(predicted_labels)

