from django.shortcuts import render
from django.http import HttpResponse

from Face_Recognition.API_Tools.face_API import face_result
from . models import Image_model as mod
from ..API_Tools.face_API import face_result
# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'FaceApp/index.html')
    elif request.method == "POST":
        image_to_eval = request.POST.get('Image')
        image_result = face_result(image_to_eval, 20)

