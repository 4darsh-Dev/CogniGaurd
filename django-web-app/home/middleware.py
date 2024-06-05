# capturing visitor information and storing it in the database

from .models import Visitor
from django.utils.deprecation import MiddlewareMixin
import datetime

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.session.get('has_visited'):
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT', '<unknown>')
            referer = request.META.get('HTTP_REFERER', None)
            path = request.path
            method = request.method

            Visitor.objects.create(
                ip_address=ip_address,
                user_agent=user_agent,
                referer=referer,
                path=path,
                method=method,
                timestamp=datetime.datetime.now()  # Add timestamp if not already present
            )
            
            request.session['has_visited'] = True
            request.session['visited_at'] = str(datetime.datetime.now())  # Store visit time
