from django.shortcuts import render, redirect
from .popup_detect_ml import predict
from django.http import JsonResponse
from json import dump
import io
import base64
from PIL import Image

# Create your views here.


def index(request):
    return render(request, "index.html")


def faqs(request):
    return render(request, "faqs.html")


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


def reportDp(request):
    return render(request, "report.html")


def about(request):
    return render(request, "about.html")
