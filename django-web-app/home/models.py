from django.db import models

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
    
# saving dark pattern data to the database
class DarkPatternsData(models.Model):
    
    website_url = models.URLField()
    dark_pattern_label = models.CharField(max_length=255)
    dark_text = models.TextField()

    def __str__(self):
        return f"{self.website_url} - Dark Pattern: {self.dark_pattern_label}"