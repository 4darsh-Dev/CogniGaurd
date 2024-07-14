# api/tasks.py

from celery import shared_task
from .models import DarkPatternsData
from .dp_scrape import dark_sentence_list
from .predict_darkp import find_dark_pattern
import csv
from celery_progress.backend import ProgressRecorder


@shared_task(bind=True)
def process_url(self, url):
    progress_recorder = ProgressRecorder(self)
    
    progress_recorder.set_progress(1, 100, f"Checking existing data for {url}")
    existing_data = DarkPatternsData.objects.filter(website_url=url).exists()
    if existing_data:
        dp_data = list(DarkPatternsData.objects.filter(website_url=url).values())
        return {"message": "Data already exists for this URL", "data": dp_data}
    
    progress_recorder.set_progress(10, 100, f"Scraping {url}")
    scrape_output, sentenceFile = dark_sentence_list(url)
    
    progress_recorder.set_progress(50, 100, "Processing scraped data")
    with open("sentences.csv", 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for row in reader)
        csvfile.seek(0)
        next(reader)  # Skip header
        for i, row in enumerate(reader):
            sentence = row['sentence']
            processed_result = find_dark_pattern(sentence)
            DarkPatternsData.objects.create(
                website_url=url,
                dark_pattern_label=processed_result,
                dark_text=sentence
            )
            progress_recorder.set_progress(50 + int((i / total_rows) * 40), 100, f"Processed {i+1} of {total_rows} sentences")
    
    progress_recorder.set_progress(90, 100, "Finalizing results")
    dp_data = list(DarkPatternsData.objects.filter(website_url=url).values())
    return {"message": "Data processed and saved", "data": dp_data}