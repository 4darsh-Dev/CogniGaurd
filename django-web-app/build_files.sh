#!/bin/bash
# Install pip and virtualenv if necessary
python3.12 -m venv venv
source venv/bin/activate

# make migrations
python manage.py migrate
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic 
