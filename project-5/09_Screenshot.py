
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import nxt.locator
from nxt.motor import *
from nxt.sensor import *


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = True
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

(w, h) = (640, 480)
x = 340
y = 200
r = 30
cnt = 100 

for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array    
    frameClone = frame.copy()
    
    text = str(frameClone[y, x])
    org = (x, y)
    fontFace = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frameClone, text, org, fontFace, 2, white, 4)
    
    
    cv2.line(frameClone, (x, 0), (x, h), green)
    cv2.line(frameClone, (0, y), (w, y), green)
    cv2.circle(frameClone, (x, y), r, green)
    
    cv2.imshow("Camera", frameClone)
    rawCapture.truncate(0)
    
    c = cv2.waitKey(1) & 0xFF
    if c == ord('b'):  # quit
        break
    elif c == ord('w'):  # point up
        y = y-5
        
    elif c == ord('s'):  # point down
        y = y+5
 
    elif c == ord('a'): # point left
        x = x-5
 
    elif c == ord('d'): # point right
        x = x+5
 
    elif c == ord('q'): # rétrécir cerlce
        r = r-5
    elif c == ord('e'): # agrandir cerlce
        r = r+5
    elif c == ord('p'):
        fileName = 'frame' + str(cnt) + '.png'
        cv2.imwrite(fileName, frameClone)
        cnt += 1
        print(fileName)
        

print("quit")





