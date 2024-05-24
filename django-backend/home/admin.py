from django.contrib import admin

# Register your models here.

from .models import DarkPatternReport, FAQData

admin.site.register(DarkPatternReport)
admin.site.register(FAQData)

