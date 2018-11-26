## import the necessary modules
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

import nxt.locator
from nxt.motor import *
from nxt.sensor import *

# initialize the LEGO MINDSTORMS NXT
b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)

touch = Touch(b, PORT_1)
light = Light(b, PORT_2)
sound = Sound(b, PORT_3)
us = Ultrasonic(b, PORT_4)

steering_gain = 0.1
speed = 20
    
## initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = True
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

(w, h) = (640, 480)
x = 320
y = 240
r = 50

## capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array    
    frameClone = frame.copy()
    
    text = str(frameClone[y, x])
    org = (x, y)
    fontFace = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frameClone, text, org, fontFace, 2, black, 4)
    
    cv2.line(frameClone, (x, 0), (x, h), red)
    cv2.line(frameClone, (0, y), (w, y), red)
    cv2.circle(frameClone, (x, y), r, red)
    
    cv2.imshow("Camera", frameClone)
    rawCapture.truncate(0)
    
    c = cv2.waitKey(1) & 0xFF
    if c == ord('b'):  # quit
        break
    elif c == ord('w'):  # move point up
        y = y-5
    elif c == ord('s'):  # move point down
        y = y+5
    elif c == ord('d'):  # move point to the right
        x = x+5
    elif c == ord('a'):  # move point to the left
        x = x-5
    elif c == ord('q'):  # bigger circle
        r = r+5
    elif c == ord('e'):  # shorter circle
        r = r-5    
