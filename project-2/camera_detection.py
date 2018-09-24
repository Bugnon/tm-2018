##import modules
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np

##initialization of the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = True
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
magenta = (127, 0, 255)



##color detection function
def colorDetection (colorBgr,colorbGr,colorbgR,squareSize,squareColor,who):
    if bl < colorBgr and gr<colorbGr and re>colorbgR:
        #take a square and check color
        q = 0          
        for yy in range (y, y+squareSize, 8):
            for xx in range (x, x+squareSize, 8):
                bb,gg,rr=frameClone[y, x]
                if bb < colorBgr and gg < colorbGr and rr > colorbgR:
                    q = q + 1
                    #if enough color : positive detection
                    if [q>70]:
                        cv2.rectangle(frameClone, (y,x), (x+squareSize,y+squareSize), squareColor)
                        print (who)


for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = f.array    
    frameClone = frame.copy()
    
    dx=80
    #take every pixel and check color   
    for y in range (0, 480, dx):
        cv2.line(frameClone, (0, y), (640, y), green)
        for x in range (0, 640, dx):
            cv2.line(frameClone, (x, 0), (x, 480), green)
            bl,gr,re=frameClone[y+1, x+1]
            colorDetection(50,50,200,40,blue,"man")
         
    cv2.imshow("Camera", frameClone)
    rawCapture.truncate(0)                    
    
    c = cv2.waitKey(1) & 0xFF
    if c == ord('q'):  # quit
        break