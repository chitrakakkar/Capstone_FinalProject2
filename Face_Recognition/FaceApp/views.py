from django.shortcuts import render
from django.http import HttpResponse
from . models import Image_model as mod
# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'FaceApp/index.html')
    # elif request.method == "POST":
    #     image_data = open("/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/"
    #                       "Face_Recognition/FaceApp/static/test.jpg", "rb").read()
    #     return HttpResponse(image_data, content_type="image/png")
    #

