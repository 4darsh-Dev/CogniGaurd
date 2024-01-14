from django.db import models

# Create your models here.


class WebsiteTransparencyScore(models.Model):
    website_name = models.CharField(max_length=255, unique=True)
    transparency_score = models.FloatField()

    def __str__(self):
        return f"{self.website_name} - Transparency Score: {self.transparency_score}"
