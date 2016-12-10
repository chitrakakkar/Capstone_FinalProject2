# Followed https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/face_detection/faces.py
#!/usr/bin/env python
# Copyright 2015 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Draws squares around faces in the given image."""
import os
import sys
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

# [START get_vision_service]


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return apiclient.discovery.build('vision', 'v1', credentials=credentials)


# [END get_vision_service]


def detect_face(face_file, max_results=20):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of dicts with information about the faces in the picture.
    """
    image_content = face_file.read()

    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('utf-8')
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
    with open(face_file, 'rb') as image:
        faces = detect_face(image)
        im = Image.open(image)
        pie_im_list =[]
        for face in range(0, len(faces)):
            face_result = faces['responses'][0]['faceAnnotations']
            # face_result = faces['responses']
            for things in face_result:
                # vertices_to_draw_poly = faces['responses'][0]['faceAnnotations'][0]["boundingPoly"]['vertices']
                vertices_to_draw_poly = things["boundingPoly"]['vertices']
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
                draw.line(box + box[0:2], width=5, fill='#00ff00')
                text_x_position = (float(box[0]) + float(box[2])) / 2
                text_y_position = (float(box[1]) + float(box[3])) / 2 - 20
                text_position = (text_x_position, text_y_position)
                draw.text((text_position,), str(face_result.index(things)), (255, 255, 255))
                #im.show()
        #im.save(r'/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition/media/Image_Analysed.jpg')
        return im, pie_im_list


def draw_pie_chart(get_expression, image_number):
 exprresion_dict ={'UNKNOWN':1.39, 'VERY_UNLIKELY' : 4.17 , 'UNLIKELY':6.94  ,'POSSIBLE':12.50  ,'VERY_LIKELY': 50.00 } # 180 Degree out of 360
 # make a square figure and axes
 fraction_division = ()
 # The slices will be ordered and plotted counter-clockwise.
 labels = ['sorrowLikelihood', 'joyLikelihood', 'angerLikelihood', 'surpriseLikelihood']
 for label in labels:
      figure(image_number, figsize=(6, 6))
      ax = axes([0.1, 0.1, 0.8, 0.8])
      Temp_Tuple=()
      Temp_Tuple = (exprresion_dict.get(get_expression[label]),)
      fraction_division = fraction_division + Temp_Tuple
 pie(fraction_division, labels=labels,
         autopct='%1.1f%%', colors=('#4C59FF', '#33D90D', '#DB1200', '#FFB21A',), shadow=True, startangle=90)
     # The default startangle is 0, which would start
     # the Frogs slice on the x-axis.  With startangle=90,
     # everything is rotated counter-clockwise by 90 degrees,
     # so the plotting starts on the positive y-axis.
 title('Face ' + str(image_number)+ ' Expressions', bbox={'facecolor': '0.8', 'pad': 5})
 pie_chart_file = r'/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition/media/image' + str(image_number)+ '.png'
 savefig(pie_chart_file, transparent=True)
 print("Blurred Faces found")
 return pie_chart_file




# if __name__ == '__main__':
#     face_file_path = r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/test3.jpg"
#     face_result(face_file_path, 20)

# def face():
#     face_file_path = r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/Face_Recognition/media/download.jpg"
#     status = face_result(face_file_path, 20)
#     return status

