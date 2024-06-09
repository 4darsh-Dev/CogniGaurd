from .models import Visitor

def visitor_count(request):
    count = Visitor.objects.count()
    return {'visitor_count': count}