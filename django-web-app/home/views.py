from django.shortcuts import render, redirect
# from .popup_detect_ml import predict
from django.http import JsonResponse
from json import dump

from .models import DarkPatternReport,FAQData,DarkPatternsData


from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def faqs(request):
    faqs = FAQData.objects.all()
    return render(request, "faqs.html", {"faqs": faqs})
    

def termsConditions(request):
    return render(request, "termsConditions.html")

def knowDp(request):
    return redirect("/")



def about(request):
    return render(request, "about.html")


# for searching dark patterns 

def detected_dp(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
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

        # Check for erroneous parameters
        if len(description) < 5:
            error_msg = "Description must be at least 5 characters long. Please try again."
            messages.error(request, error_msg)
            return render(request, 'report.html', {"error_message": error_msg})

        # Save the values in the database using the DarkPatternReport model
        report = DarkPatternReport(
            name=name,
            email=email,
            website_name=website_name,
            dark_pattern_type=dark_pattern_type,
            description=description
        )
        report.save()

        # On successful submission
        success_msg = "Your response has been recorded successfully!"
        messages.success(request, success_msg)
        return render(request, "report.html", {"error_message": success_msg})  # Redirect to a success page or another URL

    return render(request, "report.html")




