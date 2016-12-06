from django.shortcuts import render
from django.http import HttpResponse
import sys, os
sys.path.append(r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition")
os.environ['PATH'] = (r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition;"
                      + os.environ['PATH'])

from . models import Image_model as mod
from Face_Recognition.API_Tools.face_API import *
# from Face_Recognition.API_Tools.face_API import face_result

# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'FaceApp/index.html')
    elif request.method == "POST":
        image_to_eval = request.POST.get('Image')
        image_result = face_result(image_to_eval, 20)
        return render(image_result, 'FaceApp/index.html')

