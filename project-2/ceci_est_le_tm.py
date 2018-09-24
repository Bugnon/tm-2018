##import modules
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

import nxt.locator
from nxt.motor import *
from nxt.sensor import *

##initialization of nxt
b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
us = Ultrasonic(b, PORT_4)

##variables
steering_gain = 0.1
speed = 20

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

##follow
##capture frame
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = f.array    
    frameClone = frame.copy()
    # analyze the line in the lower part of the image (y=400)
    # only look at the red pixel, as it has the highest amplitude

    # find the minimum and maximum values of the derivative
    d0=0
    minval = 255
    maxval = -255
    minpos = 0
    maxpos = 0
    for x in range(0, 640, 10):
        d = frameClone[400, x, 2]
 
        # find minimum and maximum change
        dif = int(d)-int(d0)
        d0 = d
        if dif < minval and x != 0:
            minval = dif
            minpos = x
        if dif > maxval and x != 0:
            maxval = dif
            maxpos = x         
        cv2.circle(frameClone, (x, 400-d), 5, red)
        cv2.circle(frameClone, (x, 400-dif), 3, blue)


    state = int((maxpos+minpos)/2)
    target = 320
    error = target-state
    
    steering = int(steering_gain * error)
    m_left.run(speed-steering, True)
    m_right.run(speed+steering, True)
    
    cv2.line(frameClone, (maxpos, 0), (maxpos, 480), green)
    cv2.line(frameClone, (minpos, 0), (minpos, 480), green)

    cv2.line(frameClone, (0, 400), (640, 400), green)
    cv2.circle(frameClone, (target, 400), 50, green)
    
    cv2.imshow("Camera", frameClone)
    rawCapture.truncate(0)
    #take every pixel and check if red   
    for y in range (0, 480, 10):
        for x in range (0, 640, 10):
            
            if bl<50 and g<50 and r>200:
                #take a rectangle and check if red
                q = 0
                cv2.rectangle(frameClone, (x,y), (x+20,y+20), magenta)          
                for yy in range (y, y+20, 2):
                    for xx in range (x, x+20, 2):
                        [xx, yy] = (bb, gg, rr)
                        if [bb<50] and [gg<50] and [rr>200]:
                             q = q + 1
            if [q>70]:
                homme = true
            else:
                homme = false
                    
                    
    
    c = cv2.waitKey(1) & 0xFF
    if c == ord('q'):  # quit
        break
    elif c == ord('g'):  # go
        speed = 20
    elif c == ord('s'):  # stop
        speed = 0

# release the motors
m_left.idle()
m_right.idle()