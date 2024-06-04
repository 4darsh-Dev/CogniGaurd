from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse

# Create your views here.
from .models import WebsiteTransparencyScore, DarkPatternsData, DpRequest

from scraping.dp_scrape import get_scrape_data,dark_sentence_list

# Setup for DRF views
from rest_framework import generics,permissions

from .serializers import DpRequestSerializer

import pandas as pd
from .predict_darkp import find_dark_pattern

# For submitting the URL to the model
dpCond = False

class MessageCreateView(generics.CreateAPIView):
    dpCond = True
    queryset = DpRequest.objects.all()
    serializer_class = DpRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']
    

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


# Checking for existing data and then saving the dark patterns data 
def dpData(url):

    if url:
        # Check if the URL exists in DarkPatternsData model
        existing_data = DarkPatternsData.objects.filter(website_url=url).exists()

        if existing_data:
            # If the URL already exists, do nothing
            # checking the result


            dp_data = DarkPatternsData.objects.filter(website_url=url).values()
            print(dp_data)
            return JsonResponse({"message": "Data already exists for this URL","data": list(dp_data)})

        
            
        else:
            
            #  scrape data from the URL using get_scrape_data function
            scrape_output, sentenceFile = dark_sentence_list(url)
            print(scrape_output)

            # Opening the sentences file
            df = pd.read_csv("sentences.csv")

            # Process each sentence
            for _, row in df.iterrows():
                sentence = row['sentence']
                processed_result = find_dark_pattern(sentence)
                print(f"{sentence}: {processed_result}")

                dark_patterns_data = DarkPatternsData.objects.create(
                website_url=url,
                dark_pattern_label=processed_result,  # Replace with the appropriate l
                dark_text=sentence  # Replace with the scraped data
            )
            # Predicting the dark pattern
            

            # Save the scraped data to DarkPatternsData model
            

            return "Data saved to DarkPatternsData model"

    else:
        return "URL parameter is missing in the request"
    

# For viewing the list of URLs submitted
class MessageListView(generics.ListAPIView):
    queryset = DpRequest.objects.all()
    serializer_class = DpRequestSerializer
    http_method_names = ['get']



# For viewing the details of a specific URL

## You need to ensure that it doesn't call the dpData function if the dpCond is False

    # Fetching urls from model
    dpUrls = DpRequest.objects.all()
    urlLen = len(dpUrls)
    myDpUrl = dpUrls[urlLen-1].url
    print(dpUrls)
    myOutput = dpData(myDpUrl)
    print(myOutput)
    dpCond = False



    






















