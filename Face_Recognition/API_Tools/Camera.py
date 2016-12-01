import time
from SimpleCV import Camera
import os
import sys
from types import *



sys.path.append(r"/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/SimpleCV")
os.environ['PATH'] = (r"/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/SimpleCV;"
                          + os.environ['PATH'])

cam = Camera()
time.sleep(0.1)  # If you don't wait, the image will be dark
img = cam.getImage()
img.save("simplecv.png")