"""
URL configuration for cogniguard project.

"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Admin panel customization
admin.site.site_header = "CogniGuard Admin"
admin.site.site_title = "CogniGuard Admin Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("logout/", RedirectView.as_view(url="/admin/logout/")),
    path("", include("home.urls")),
    
]
# vercel deployment url configuration

# # vercel deployment conf
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)