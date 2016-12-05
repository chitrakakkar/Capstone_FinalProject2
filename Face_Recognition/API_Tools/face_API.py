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
#from test import face



sys.path.append(r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2")
os.environ['PATH'] = (r" /Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2;"
                      + os.environ['PATH'])

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join("/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/", 'CapstoneFinalProject-5be08202b757.json')


import base64
from apiclient import channel , discovery, errors , http, mimeparse, model, schema #discovery #from apiclient
import apiclient
from oauth2client.client import GoogleCredentials
from PIL import Image
from PIL import ImageDraw
import json


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
            faces = detect_face(image, max_results)
            im = Image.open(image)
            for face in range(0, len(faces)):
                face_result = faces['responses'][0]['faceAnnotations']
                for things in face_result:
                    # vertices_to_draw_poly = faces['responses'][0]['faceAnnotations'][0]["boundingPoly"]['vertices']
                    vertices_to_draw_poly = things["boundingPoly"]['vertices']
                    draw = ImageDraw.Draw(im)
                    box = ()
                    for v in vertices_to_draw_poly:
                        temp = (
                        v.get('x', vertices_to_draw_poly[0]['x']), v.get('y', vertices_to_draw_poly[0]['y']))
                        box = box + temp
                    draw.line(box + box[0:2], width=5, fill='#00ff00')
        im.save('Image_analysed.jpg')


if __name__ == '__main__':
    face_file_path = r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/test.jpg"
    face_result(face_file_path, 20)
