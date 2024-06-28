from django.contrib import admin
from .models import WebsiteTransparencyScore, DarkPatternsData,DpRequest

# Register your models here.
admin.site.register(WebsiteTransparencyScore)
admin.site.register(DarkPatternsData)
admin.site.register(DpRequest)
