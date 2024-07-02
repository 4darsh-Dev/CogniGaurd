from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import WebsiteTransparencyScore, DarkPatternsData, DpRequest
from .dp_scrape import get_scrape_data, dark_sentence_list
from rest_framework import generics, permissions
from .serializers import DpRequestSerializer
from .predict_darkp import find_dark_pattern
import csv

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
    website_name = "example.com"  # Replace with the actual website name
    WebsiteTransparencyScore.objects.update_or_create(
        website_name=website_name,
        defaults={'transparency_score': tScore}
    )
    return tScore

def dpData(url):
    if url:
        existing_data = DarkPatternsData.objects.filter(website_url=url).exists()
        if existing_data:
            dp_data = DarkPatternsData.objects.filter(website_url=url).values()
            print(dp_data)
            return JsonResponse({"message": "Data already exists for this URL", "data": list(dp_data)})
        else:
            scrape_output, sentenceFile = dark_sentence_list(url)
            print(scrape_output)
            
            with open("sentences.csv", 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    sentence = row['sentence']
                    processed_result = find_dark_pattern(sentence)
                    print(f"{sentence}: {processed_result}")
                    dark_patterns_data = DarkPatternsData.objects.create(
                        website_url=url,
                        dark_pattern_label=processed_result,
                        dark_text=sentence
                    )
            
            return "Data saved to DarkPatternsData model"
    else:
        return "URL parameter is missing in the request"

class MessageListView(generics.ListAPIView):
    queryset = DpRequest.objects.all()
    serializer_class = DpRequestSerializer
    http_method_names = ['get']

# For viewing the details of a specific URL
## You need to ensure that it doesn't call the dpData function if the dpCond is False


dpUrls = DpRequest.objects.all()
urlLen = len(dpUrls)
if urlLen > 0:
    myDpUrl = dpUrls[urlLen-1].url
    print(dpUrls)
    myOutput = dpData(myDpUrl)
    print(myOutput)
dpCond = False