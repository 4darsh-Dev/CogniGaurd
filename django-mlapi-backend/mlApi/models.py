from django.db import models

# Create your models here.

# beta feature - saving the transparency score to the database
class WebsiteTransparencyScore(models.Model):
    website_name = models.CharField(max_length=255, unique=True)
    transparency_score = models.FloatField()



    def __str__(self):
        return f"{self.website_name} - Transparency Score: {self.transparency_score}"

# saving dark pattern data to the database
class DarkPatternsData(models.Model):
    
    website_url = models.URLField()
    dark_pattern_label = models.CharField(max_length=255)
    dark_text = models.TextField()

    def __str__(self):
        return f"{self.website_url} - Dark Pattern: {self.dark_pattern_label}"


# saving each request to the database
class DpRequest(models.Model):


    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.url } at {self.created_at}"
    
    
    


    
