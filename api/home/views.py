from django.shortcuts import render, redirect
from .popup_detect_ml import predict
from django.http import JsonResponse
from json import dump
import io
import base64
from PIL import Image

from .models import DarkPatternReport
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def faqs(request):
    return render(request, "faqs.html")

def termsConditions(request):
    return render(request, "termsConditions.html")

def knowDp(request):
    return redirect("/")

def popup_detect(request):
    # img = data_url_to_image(request.GET.get('img', ''))
    # return JsonResponse(dump(predict(img)))

    # get image data url
    img = request.GET.get("img", "")

    if img == "":
        return JsonResponse({"error": "data url empty"})

    # convert dataurl to PIL
    img = data_url_to_image(img)

    # predict the result using trained ml algo
    result = predict(img)

    # return the results
    return JsonResponse(dump(result))


def data_url_to_image(data_url):
    # Remove the header of the data URL
    header, base64_str = data_url.split(",")

    # Decode the base64 string to bytes
    decoded_image = base64.b64decode(base64_str)

    # Create a BytesIO object and read the decoded image into it
    image_data = io.BytesIO(decoded_image)

    # Open the image with PIL
    img = Image.open(image_data)

    return img


def about(request):
    return render(request, "about.html")



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
        return render(request, "report.html", {error_msg: success_msg})  # Redirect to a success page or another URL

    return render(request, "report.html")

