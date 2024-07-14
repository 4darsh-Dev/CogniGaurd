from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.

class DarkPatternReport(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website_name = models.CharField(max_length=200)
    dark_pattern_type = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.website_name} "
    
class FAQData(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

# API keys management

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=600, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=30)  # Default 30 days validity
        super().save(*args, **kwargs)

    def is_valid(self):
        return timezone.now() < self.expires_at
    


# visitor count model using middleware
# class Visitor(models.Model):
#     ip_address = models.GenericIPAddressField()
#     user_agent = models.CharField(max_length=255)
#     referer = models.URLField(null=True, blank=True)
#     path = models.CharField(max_length=255)
#     method = models.CharField(max_length=10)
#     timestamp = models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         return f"{self.ip_address} at {self.timestamp}"

#     class Meta:
#         verbose_name = "Visitor"
#         verbose_name_plural = "Visitors"