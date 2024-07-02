#!/bin/sh

# Run Django migrations
echo "Running migrations..."
python manage.py migrate

exec "$@"