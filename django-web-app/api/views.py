from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import WebsiteTransparencyScore, DarkPatternsData, DpRequest
from .dp_scrape import get_scrape_data, dark_sentence_list
from rest_framework import generics, permissions
from .serializers import DpRequestSerializer, DarkPatternsDataSerializer
from .predict_darkp import find_dark_pattern
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import process_url

from celery_progress.backend import Progress
from celery.result import AsyncResult


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



class AnalyzeURLView(APIView):
    def post(self, request):
        url = request.data.get('url')
        if not url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        existing_data = DarkPatternsData.objects.filter(website_url=url).exists()
        if existing_data:
            dp_data = DarkPatternsData.objects.filter(website_url=url)
            serializer = DarkPatternsDataSerializer(dp_data, many=True)
            return Response({"status": "completed", "data": serializer.data})
        
        task = process_url.delay(url)
        return Response({"status": "processing", "task_id": task.id})

class TaskStatusView(APIView):
    def get(self, request, task_id):
        task = process_url.AsyncResult(task_id)
        if task.ready():
            result = task.result
            dp_data = DarkPatternsData.objects.filter(website_url=result['url'])
            serializer = DarkPatternsDataSerializer(dp_data, many=True)
            return Response({"status": "completed", "data": serializer.data})
        elif task.failed():
            return Response({"status": "failed", "error": str(task.result)})
        else:
            return Response({"status": "processing"})
        
class TaskStatusView(APIView):
    def get(self, request, task_id):
        task = AsyncResult(task_id)
        if task.ready():
            if task.successful():
                result = task.result
                return Response({"status": "completed", "data": result["data"]})
            else:
                return Response({"status": "failed", "error": str(task.result)})
        else:
            return Response({"status": "processing"})

class MessageListView(generics.ListAPIView):
    queryset = DpRequest.objects.all()
    serializer_class = DpRequestSerializer
    http_method_names = ['get']

