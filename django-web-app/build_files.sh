#!/bin/bash

# make migrations
python manage.py migrate
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic 
