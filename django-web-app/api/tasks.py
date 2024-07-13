# api/tasks.py

from celery import shared_task
from .models import DarkPatternsData
from .dp_scrape import dark_sentence_list
from .predict_darkp import find_dark_pattern
import csv

@shared_task
def process_url(url):
    existing_data = DarkPatternsData.objects.filter(website_url=url).exists()
    if existing_data:
        dp_data = list(DarkPatternsData.objects.filter(website_url=url).values())
        return {"message": "Data already exists for this URL", "data": dp_data}
    
    scrape_output, sentenceFile = dark_sentence_list(url)
    
    with open("sentences.csv", 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentence = row['sentence']
            processed_result = find_dark_pattern(sentence)
            DarkPatternsData.objects.create(
                website_url=url,
                dark_pattern_label=processed_result,
                dark_text=sentence
            )
    
    dp_data = list(DarkPatternsData.objects.filter(website_url=url).values())
    return {"message": "Data processed and saved", "data": dp_data}