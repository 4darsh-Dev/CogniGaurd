from django.shortcuts import render,redirect
from django.http import JsonResponse

# Create your views here.
from .models import WebsiteTransparencyScore, DarkPatternsData

from scraping.dp_scrape import get_scrape_data



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

    if url != '':
        # Call the scraping function and get the text
    
        scraped_text = get_scrape_data(url)

        print(scraped_text)

        # Fine-tune BERT model and classify dark pattern
        # predicted_labels = fine_tune_and_classify(scraped_text)
        predicted_labels= {"Sample": "This is a Sample dark pattern"}

        # Save the dark pattern data in the DarkPatternData model
        website_url = url
        for label, dark_text in predicted_labels.items():
            dark_pattern, created = DarkPatternsData.objects.get_or_create(
                website_url=website_url,
                dark_pattern_label=label,
                defaults={'dark_text': dark_text}
            )

            # If the record already exists, update the dark_text field
            if not created:
                dark_pattern.dark_text = dark_text
                dark_pattern.save()

    return JsonResponse({"dp_data": "This is the dark pattern data"})