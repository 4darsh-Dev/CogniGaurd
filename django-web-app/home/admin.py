from django.contrib import admin

# Register your models here.

from .models import DarkPatternReport, FAQData
from django.contrib import admin
# from .models import Visitor

# visitor model

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'referer', 'path', 'method', 'timestamp')
    search_fields = ('ip_address', 'user_agent', 'referer', 'path', 'method')
    list_filter = ('method', 'timestamp')


# registering the models

# admin.site.register(Visitor, VisitorAdmin)

admin.site.register(DarkPatternReport)
admin.site.register(FAQData)

