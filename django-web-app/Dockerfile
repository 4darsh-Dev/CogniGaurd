# Pull python base image
FROM python:3.12.0-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/django-web-app
ENV APP_HOME=${HOME}/web

# Create app user and necessary directories
RUN mkdir -p $HOME && \
    addgroup --system app && \
    adduser --system --group app && \
    mkdir $APP_HOME ${APP_HOME}/staticfiles ${APP_HOME}/media

# Set work directory
WORKDIR $APP_HOME

# Copy requirements.txt
COPY ./requirements.txt $APP_HOME

# Install python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install other dependencies (Debian)
RUN apt-get update && apt-get install -y --no-install-recommends netcat && rm -rf /var/lib/apt/lists/*

# Copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# Remove Windows line endings and make entrypoint.sh executable
RUN sed -i 's/\r$//g' ${APP_HOME}/entrypoint.sh && chmod +x ${APP_HOME}/entrypoint.sh

# Copy project
COPY . $APP_HOME

# Set ownership and permissions for app user on app directory
RUN chown -R app:app $APP_HOME && chmod -R 777 $APP_HOME

# Switch to app user
USER django-web-app

# Collect static files
RUN python manage.py collectstatic --no-input --clear

# Expose port 8000
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=5s \
            --timeout=3s \
            CMD curl --fail http://localhost:8000/health-check || exit 1

# Run entrypoint.sh
ENTRYPOINT ["/home/django-web-app/web/entrypoint.sh"]

# Run application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "--timeout", "90", "--access-logfile", "/home/django-web-app/web/access.log", "--error-logfile", "/home/django-web-app/web/error.log", "cogniguard.wsgi:application"]