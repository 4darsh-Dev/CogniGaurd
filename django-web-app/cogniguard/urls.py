"""
URL configuration for cogniguard project.

"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

# Admin panel customization
admin.site.site_header = "CogniGuard Admin"
admin.site.site_title = "CogniGuard Admin Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("logout/", RedirectView.as_view(url="/admin/logout/")),
    path("", include("home.urls")),

    # for rendering reset password cnf template
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    # ensuring password reset completed successfully
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

     path('accounts/', include('allauth.urls')), # all OAuth operations will be performed 

     # api urls
     path("api/", include("api.urls")),
     
]
# # vercel deployment url configuration

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# custom 404 page 
handler404 = 'home.views.handler404'