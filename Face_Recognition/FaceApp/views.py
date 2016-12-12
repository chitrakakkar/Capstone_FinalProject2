from io import BytesIO


from django.shortcuts import render
from . models import Image_model, chart_model
from .API_Tools.face_API import *
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from numpy.core.tests.test_mem_overlap import xrange
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
        chart_stitched_image = convert_chart_file(chart_image_stiching(pi_im_list))
        # for pie in pi_im_list:
        #     chart_image = convert_pillow_file2(pie)
        pie_chart_data = Image_model.objects.create(image=chart_stitched_image)
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


# convert png to jpeg and use convert_pillow_file to convert into django file
def convert_pillow_file2(file_to_convert):
    im = Image.open(file_to_convert)
    bg = Image.new("RGB", im.size, (255, 255, 255))
    # im.thumbnail(size)
    bg.paste(im, (0, 0), im)
    bg.save("file.jpg", quality=95)
    bg_coverted_file= convert_chart_file(bg)
    return bg_coverted_file


def chart_image_stiching(pi_im_list):
    color = (255, 255, 255)
    new_im = Image.new(mode='RGBA', size=(600, 600))
    list_of_CO=[(0, 0), (0, 300), (300, 0), (300, 300)]

    for pie in pi_im_list:
        # resize = 300
        im = Image.open(pie)
        # width =  float(im.size[0])
        # height = float(im.size[1])
        # newwidth = ( 300/ float(im.size[0]))
        # print ("w precent", wpercent)
        # hsize = int((float(im.size[1]) * float(wpercent)))
        #
        # im.resize((basewidth,hsize),Image.NEAREST)
        im= im.resize((300, 300),Image.NEAREST)
        # im.show()
        new_im.paste(im, (list_of_CO[pi_im_list.index(pie)]))
    # new_im.show()
    return new_im
