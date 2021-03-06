# Followed https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/face_detection/faces.py
import os
import sys

from PIL import ImageFont

sys.path.append(r"/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
sys.path.append(r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2")
os.environ['PATH'] = (r" /Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2;"
                      + os.environ['PATH'])
os.environ['PATH'] = (r" Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages;"
                      + os.environ['PATH'])

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join("/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/", 'CapstoneFinalProject-5be08202b757.json')
# from matplotlib.pyplot import title
# from matplotlib.figure import Figure as figure
# from matplotlib.axes import Axes as axes
import matplotlib.pylab
__doc__ = matplotlib.pylab.__doc__
from pylab import *
import base64
import apiclient
from oauth2client.client import GoogleCredentials
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageDraw

# [START get_vision_service] # create a service object based on the API's discovery document,
# which describes the API to the SDK #
# followed this tutorial:- https://cloud.google.com/vision/docs/face-tutorial


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return apiclient.discovery.build('vision', 'v1', credentials=credentials)


# [END get_vision_service]


def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of dicts with information about the faces in the picture.
    """
    image_content = face_file.read()  # reading the image file as binary strings
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('utf-8')  # changing the binary string to text string
        },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
        }]
    }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
    })
    response = request.execute()
    # print(response)
    # return response['responses'][0]['faceAnnotations']

    return response


# This method calls detec_face method which makes an API call to get the response: A sample response is in test.py
def face_result(face_file, max_results):
    pie_im_list = []    #list to contain all charts
    # font = ImageFont.load_default().font
    with open(face_file, 'rb') as image:
        faces = detect_face(image)    # response from detect_face
        print("I am responses", faces)
        im = Image.open(image)           # opens a file as an image
        for face in range(0, len(faces)):
            try:
                face_result = faces['responses'][0]['faceAnnotations'] # index for the emotions I wanted to extract
                # face_result = faces['responses']
                for things in face_result:

                    vertices_to_draw_poly = things["boundingPoly"]['vertices']   # extracting vertices from the response
                    pie_im_list.append(draw_pie_chart(things, face_result.index(things)))
                    # draw_pie_chart(things,face_result.index(things))
                    # im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))
                    draw = ImageDraw.Draw(im)
                    # print("The expressions for the face ", face_reult.index(things))
                    box = ()
                    for v in vertices_to_draw_poly:
                        temp = (v.get('x', vertices_to_draw_poly[0]['x']), v.get('y', vertices_to_draw_poly[0]['y']))
                        box = box + temp
                    # print("I am the box", box)
                    draw.line(box + box[0:2], width=5, fill='#00ff00')  # drawing the polygon
                    text_x_position = (float(box[0]) + float(box[2])) / 2
                    text_y_position = (float(box[1]) + float(box[3])) / 2 - 20
                    text_position = (text_x_position, text_y_position)
                    draw.text((text_position,), str(face_result.index(things)), fill='#00ff00') #draw the face number
                    #im.show()
            #im.save(r'/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition/media/Image_Analysed.jpg')
                return im, pie_im_list
            except:
                    with open('/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/cry_baby2.jpg', 'rb') as failImage:
                        fail_im = Image.open(failImage)
                        fail_im.show()
                        pie_im_list.append('/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Sad_chart.jpg')
                    return fail_im, pie_im_list


# This method uses MAtPlotLib to draw the charts, gets the emotions scraped out of Face_detect
# Followed this tutorial:-https://pythonspot.com/en/matplotlib-pie-chart/
def draw_pie_chart(get_expression, image_number):
 matplotlib.rcParams['text.color'] = 'g'
 matplotlib.rcParams['lines.linewidth'] = 5
 matplotlib.rcParams['font.size'] = 12
 # expression_dict has hard coded values for fractions for the expressions.
 exprresion_dict ={'UNKNOWN': 1.39, 'VERY_UNLIKELY': 4.17, 'UNLIKELY': 6.94, 'POSSIBLE': 12.50, 'VERY_LIKELY': 50.00} # 180 Degree out of 360
 # make a square figure and axes
 fraction_division = ()
 # The slices will be ordered and plotted counter-clockwise.
 labels = ['sorrowLikelihood', 'joyLikelihood', 'angerLikelihood', 'surpriseLikelihood']  #this matches the expression picked from API response
 for label in labels:
      figure(image_number, figsize=(6, 6))
      ax = axes([0.1, 0.1, 0.8, 0.8])
      Temp_Tuple = ()
      Temp_Tuple = (exprresion_dict.get(get_expression[label]),)  # expression dict matches the key and its value
      fraction_division = fraction_division + Temp_Tuple
 pie(fraction_division, labels=labels,
         autopct='%1.1f%%', colors=('#4C59FF', '#33D90D', '#DB1200', '#FFB21A',), shadow=True, startangle=90)   # draws the chart in different colors
     # The default startangle is 0, which would start
     # the Frogs slice on the x-axis.  With startangle=90,
     # everything is rotated counter-clockwise by 90 degrees,
     # so the plotting starts on the positive y-axis.
 title('Face ' + str(image_number)+ ' Expressions', bbox={'facecolor': '0.8', 'pad': 5})  # chart title
 pie_chart_file = r'/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition/media/image' + str(image_number)+ '.png'
 savefig(pie_chart_file, transparent=True) # saving extra set for testing
 print("Blurred Faces found")
 return pie_chart_file


# def convert_png_file2_Jpeg(file_to_convert):
#     im = Image.open(file_to_convert)
#     bg = Image.new("RGB", im.size, (255, 255, 255))
#     # im.thumbnail(size)
#     bg.paste(im, (0, 0), im)
#     bg.save("file.jpg", quality=95)
#     return bg

# if __name__ == '__main__':
#     face_file_path = r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/test3.jpg"
#     face_result(face_file_path, 20)

# def face():
#     face_file_path = r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition/media/download.jpg"
#     status = face_result(face_file_path, 20)
#     return status

