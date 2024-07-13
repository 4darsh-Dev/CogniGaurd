# capturing visitor information and storing it in the database

from .models import Visitor
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from datetime import timedelta

# class VisitorTrackingMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         current_time = timezone.now()
#         last_visit_time = request.session.get('last_visit_time')

#         if last_visit_time:
#             last_visit_time = timezone.datetime.fromisoformat(last_visit_time)
        
#         if not last_visit_time or (current_time - last_visit_time) > timedelta(hours=24):
#             ip_address = request.META.get('REMOTE_ADDR')
#             user_agent = request.META.get('HTTP_USER_AGENT', '<unknown>')
#             referer = request.META.get('HTTP_REFERER', None)
#             path = request.path
#             method = request.method

#             Visitor.objects.create(
#                 ip_address=ip_address,
#                 user_agent=user_agent,
#                 referer=referer,
#                 path=path,
#                 method=method,
#                 timestamp=current_time
#             )
            
#             request.session['last_visit_time'] = current_time.isoformat()

