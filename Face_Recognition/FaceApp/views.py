from django.shortcuts import render
from django.http import HttpResponse

from Face_Recognition.API_Tools.face_API import detect_face
from . models import Image_model as mod
# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'FaceApp/index.html')
    elif request.method =="POST":
        Image_to_eval = request.POST.get('Image')
        number_f_image_data = detect_face(Image_to_eval)

