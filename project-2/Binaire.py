import io
from picamera import PiCamera
from picamera.array import PiRGBArray

import time
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow("Frame",image)
key = cv2.waitKey(1) & 0xFF

result = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Result",result)
key = cv2.waitKey(1) & 0xFF


cv2.destroyAllWindows()
