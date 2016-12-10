from io import BytesIO
from django.shortcuts import render
from . models import Image_model, chart_model
from .API_Tools.face_API import *
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import glob, os

# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'FaceApp/index.html')
    elif request.method == 'POST':
        image_file = request.FILES.get('file')
        face_data = Image_model.objects.create(image=image_file)
        catch_face_detect_data, pi_im_list = face_result(face_data.image.path, 20)
        print("Here", pi_im_list)
        for pie in pi_im_list:
            chart_image = convert_pillow_file2(pie)
            print("type of pie", type(chart_image))
            pie_chart_data = Image_model.objects.create(image=chart_image)
        result = convert_pillow_file(catch_face_detect_data)
        analysed_face_data = Image_model.objects.create(image=result)
        return render(request, 'FaceApp/Analysed.html', {'file_name': analysed_face_data.image.url, 'Pie':pie_chart_data.image.url})


def convert_pillow_file(file_to_convert):
    tempfile = file_to_convert
    tempfile_io = BytesIO()
    tempfile.save(tempfile_io, format='jpeg')
    image_file = InMemoryUploadedFile(tempfile_io, None, 'Face_detected.jpg', 'image/jpeg', sys.getsizeof(tempfile_io), None)
    return image_file


def convert_chart_file(file_to_convert):
    tempfile = file_to_convert
    tempfile_io = BytesIO()
    tempfile.save(tempfile_io, format='jpeg')
    image_file = InMemoryUploadedFile(tempfile_io, None, 'Chart.jpg', 'image/jpeg', sys.getsizeof(tempfile_io), None)
    return image_file


def convert_pillow_file2(file_to_convert):
    im = Image.open(file_to_convert)
    bg = Image.new("RGB", im.size, (255, 255, 255))
    # im.thumbnail(size)
    bg.paste(im, (0, 0), im)
    bg.save("file.jpg", quality=95)
    bg_coverted_file= convert_chart_file(bg)
    return bg_coverted_file
