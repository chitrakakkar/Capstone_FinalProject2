from base64 import b64decode
from io import BytesIO
from io import StringIO


from django.shortcuts import render
from django.core.files.base import ContentFile
from . models import Image_model
from .API_Tools.face_API import *
from django.core.files.base import File
import PIL


from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'FaceApp/index.html')
    elif request.method == 'POST':
        image_file = request.FILES['file']
        face_data = Image_model.objects.create(image=image_file)
        result =convert_file(face_result(face_data.image.path, 20))
        #result.show()
        analysed_face_data = Image_model.objects.create(image=result)
        #pie_chart = draw_pie_chart(analysed_face_data)
        return render(request, 'FaceApp/Analysed.html', {'file_name': analysed_face_data.image.url})


def convert_file(file_to_convert):
    tempfile = file_to_convert
    tempfile_io = BytesIO()
    tempfile.save(tempfile_io, format='jpeg')
    image_file = InMemoryUploadedFile(tempfile_io, None, 'rotate.jpg', 'image/jpeg', sys.getsizeof(tempfile_io), None)
    return image_file