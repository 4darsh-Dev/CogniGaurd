from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import DarkPatternReport, FAQData
from api.models import DarkPatternsData
from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail
from django.urls import reverse
from django.core.signing import Signer, BadSignature
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone


#password reset
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# detected dp func()
from django.views.decorators.http import require_GET
from django.http import HttpResponseBadRequest

# generate token imps
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from .models import APIKey
import secrets


# health check path
def health_check(request):
    return HttpResponse("OK")

def index(request):
    return render(request, "index.html")

def faqs(request):
    faqs = FAQData.objects.all()
    return render(request, "faqs.html", {"faqs": faqs})

def termsConditions(request):
    return render(request, "termsConditions.html")

def termsOfUse(request):
    return render(request, "terms_of_use.html")

def privacyPolicy(request):
    return render(request, "privacy_policy.html")

def knowAboutDp(request):
    return render(request, "know_about_dp.html")

def about(request):
    return render(request, "about.html")

# Dashboard
# @login_required
# def dashboard(request):
#     username = request.user.username
#     return render(request, 'dashboard.html', {'username': username})

@login_required
def dashboard(request):
    api_keys = APIKey.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'api_keys': api_keys, 'username': request.user.username})

# Generate token
@login_required
def generate_token(request):
    if request.method == 'POST':
        user = request.user
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'token': str(refresh.access_token),
        })
    return JsonResponse({'error': 'Invalid request method'}, status=400)



@login_required
@csrf_exempt
def create_api_key(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Default')
        key = secrets.token_urlsafe(32)
        api_key = APIKey.objects.create(user=request.user, name=name, key=key)
        return JsonResponse({
            'id': api_key.id,
            'name': api_key.name,
            'key': api_key.key,
            'expires_at': api_key.expires_at.isoformat(),
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
@csrf_exempt
def delete_api_key(request, key_id):
    if request.method == 'POST':
        APIKey.objects.filter(id=key_id, user=request.user).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# User Authentication
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:dashboard') 
        else:
            error_message = "Invalid username or password! Please try again."
            messages.error(request, error_message)
            return render(request, "login.html", {"error_message": error_message})

    return render(request, 'login.html')

# email verification

signer = Signer()

def sendVerifyEmail(user, request):
    
    token = signer.sign(user.email)
    verify_url = request.build_absolute_uri(reverse('home:verify-email') + '?token=' + token)
    subject = 'Verify your email address'

    context = {
        'user': user,
        'verify_url': verify_url,
        'current_year': timezone.now().year
    }

    html_content = render_to_string('email_verify.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
    email.attach_alternative(html_content, "text/html")
    email.send()

def registerUser(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cnf-password']

        context = {
            'username': username,
            'email': email
        }

        if len(username) > 10:
            error_msg = "Username must be under 10 characters."
            messages.error(request, error_msg)
            return render(request, 'register.html', {"error_message": error_msg, **context})

        if len(pass1) < 8:
            error_msg = "Password must be at least 8 characters long."
            messages.error(request, error_msg)
            return render(request, 'register.html', {"error_message": error_msg, **context})

        if not username.isalnum():
            error_msg = "Username should only contain letters and numbers."
            messages.error(request, error_msg)
            return render(request, 'register.html', {"error_message": error_msg, **context})

        if pass1 != pass2:
            error_msg = "Passwords do not match!"
            messages.error(request, error_msg)
            return render(request, 'register.html', {"error_message": error_msg, **context})

        if User.objects.filter(username=username).exists():
            error_msg = "Username is already taken. Please choose a different one."
            messages.error(request, error_msg)
            return render(request, 'register.html', {"error_message": error_msg, **context})

        if User.objects.filter(email=email).exists():
            error_msg = "Email is already associated with an account."
            messages.error(request, error_msg)
            return render(request, 'register.html', {"error_message": error_msg, **context})

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False  # User is inactive until email is verified
        myuser.save()

        sendVerifyEmail(myuser, request)

        success_msg = "Your CogniGuard account has been created successfully! Please check your email to verify your account."
        messages.success(request, success_msg)
        return redirect('home:loginUser')

    return render(request, 'register.html')

def verifyEmail(request):
    token = request.GET.get('token')

    try:
        email = signer.unsign(token)
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        messages.success(request, "Email verified successfully! You can now log in.")
        return redirect('home:loginUser')
    except (BadSignature, User.DoesNotExist):
        messages.error(request, "Invalid verification link.")
        return redirect('home:registerUser')
    


def logoutUser(request):
    auth.logout(request)
    return redirect("home:home")

# For searching dark patterns
@require_GET
def detected_dp(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        if len(query) < 3:
            return HttpResponseBadRequest("Query must be at least 3 characters long")
        
        results = DarkPatternsData.objects.filter(website_url__icontains=query) | DarkPatternsData.objects.filter(dark_pattern_label__icontains=query)
        data = []
        for result in results:
            data.append({
                'website_url': result.website_url,
                'dark_pattern_label': result.dark_pattern_label,
                'dark_text': result.dark_text
            })
        return JsonResponse({'results': data})
    return render(request, 'detected_dp.html')

def reportDp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website_name = request.POST.get('website-name')
        dark_pattern_type = request.POST.get('dark-pattern-type')
        description = request.POST.get('description')

        if len(description) < 5:
            error_message = "Description must be at least 5 characters long. Please try again."
            messages.error(request, error_message)
            return render(request, 'report.html', {"error_message": error_message})

        report = DarkPatternReport(
            name=name,
            email=email,
            website_name=website_name,
            dark_pattern_type=dark_pattern_type,
            description=description
        )
        report.save()

        error_message = "Your response has been recorded successfully!"
        messages.success(request, error_message)
        return render(request, "report.html", {"error_message": error_message})

    return render(request, "report.html")


# password reset class
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly."
    success_url = reverse_lazy('home:home')



# page not found
def handler404(request, exception):
    return render(request, 'custom_404.html', status=404)