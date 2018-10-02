"""
Author:  Erkin
Date:  19 June 2018
File:  02_camera
This program draws a vertical and horizontal line at (x, y)
"""

## import the necessary modules
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

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
pink = (200, 200, 255)

(w, h) = (640, 480)
x = 200
y = 300
r = 70

## capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array
    frameClone = frame.copy()
    
    print(frameClone[y, x])
    text = str(frameClone[y, x])
    org = (x, y)
    fontFace = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frameClone, text, org, fontFace, 2, red, 4)
    
    cv2.line(frameClone, (x, 0), (x, h), blue)
    cv2.line(frameClone, (0, y), (w, y), blue)
    cv2.circle(frameClone, (x, y), r, pink)
    
    
    cv2.imshow("Camera", frameClone)
    rawCapture.truncate(0)
    
    c = cv2.waitKey(1) & 0xFF
    if c == ord('q'):  # quit
        break
    elif c == ord('g'):  # go
        y = y+10
    elif c == ord('s'):  # stop
        r = r+10
    
