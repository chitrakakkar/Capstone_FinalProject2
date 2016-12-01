#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Draws squares around faces in the given image."""
import os
import sys


#
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


# def highlight_faces(image, faces, output_filename):
#     """Draws a polygon around the faces, then saves to output_filename.
#     Args:
#       image: a file containing the image with the faces.
#       faces: a list of faces found in the file. This should be in the format
#           returned by the Vision API.
#       output_filename: the name of the image file to be created, where the
#           faces have polygons drawn around them.
#     """
#     im = Image.open(image)
#     draw = ImageDraw.Draw(im)
#
#     for face in faces:
#         box = [(v.get('x', 0.0), v.get('y', 0.0))
#                for v in face['fdBoundingPoly']['vertices']]
#         draw.line(box + [box[0]], width=5, fill='#00ff00')
#
#     im.save(output_filename)


def main(input_filename, output_filename, max_results):

    with open(input_filename, 'rb') as image:
        # faces = detect_face(image, max_results)['responses'][0]['faceAnnotations']
        faces = detect_face(image, max_results)
        #face is a list of faces found in image. If 4 faces, then faceAnnotation contains
        # analysis of 4 faces in a  list
        # to fetch first face, use response['responses'][0]['faceAnnotations'][0]
        # to fetch 'joyLikelihood' of first face, use response['responses'][0]['faceAnnotations'][0]['joyLikelihood']
        for face in range(0, len(faces)):
            temp = {}
            temp = faces['responses'][0]['faceAnnotations']
            face_reult =[]
            for things in temp:
                print("The expressions for the face ", temp.index(things))
                print("The blurred expressions are", things['blurredLikelihood'])
                print("The joy likelyhood is", things['joyLikelihood'])
                print("The anger likelyhood is", things['angerLikelihood'])

            return face_reult

        # print('Found {} face{}'.format(
        #     len(faces), '' if len(faces) == 1 else 's'))


        # print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        # image.seek(0)
        # highlight_faces(image, faces, output_filename)


if __name__ == '__main__':
    main(r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject2/test.jpg", 'out.jpg', 20)
