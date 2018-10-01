#import modules
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

import nxt.locator
from nxt.motor import *
from nxt.sensor import *

##initialization of nxt
b = nxt.locator.find_one_brick()

motorLeft = Motor(b, PORT_B)
motorRight = Motor(b, PORT_C)

##variables
steeringGain = 0.1
speed = 20

#initialization of the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = True
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))

#colors
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
magenta = (127, 0, 255)
yellow = (255, 255, 0)
#color detection square size
dx=30
#priority coefficient
manCoeff = 10
oldManCoeff = 7
childCoeff = 15
animalCoeff = 3
#loop variable
loop = 0
loop2 = 0
choice = 0

#main loop, is used to reset color detection
while loop ==0:

    #person count by default
    manLeft = 0
    oldManLeft = 0
    childLeft = 0
    animalLeft = 0
    manRight = 0
    oldManRight = 0
    childRight = 0
    animalRight = 0
    #color detection reset
    colorDetection = 0
    loop2 = 0
    
    #second loop, car will go left/right if there is a choice to make (it will break image analysis loop)
    while loop2 ==0:
        
        #reset priority
        leftPriority = 0
        rightPriority = 0
        
        #image analysis loop
        for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            frame = f.array    
            frameClone = frame.copy()
            
            #color detection
            if colorDetection == 0:
                #take every pixel and check color   
                for y in range (160, 320, dx):
                    for x in range (0, 640, dx):
                        bl,gr,re=frameClone[y, x]
                #red check (man)
                        if bl < 50 and gr < 50 and re > 200:
                        #take a square and check if red
                            redRate = 0          
                            for yy in range (y, y+dx, 8):
                                for xx in range (x, x+dx, 8):
                                    bb,gg,rr=frameClone[y, x]
                                    if bb < 50 and gg < 50 and rr > 200:
                                        redRate +=1
                                        #if enough color : positive detection
                                        if [redRate>70]:
                                            cv2.rectangle(frameClone, (x,y), (x+dx,y+dx), green)
                                            #locate detection (left or right)
                                            if x<320 :
                                                manLeft +=1
                                            else :
                                                manRight +=1
                #blue check (old man)
                        if bl > 200 and gr < 50 and re < 50:
                        #take a square and check if blue
                            blueRate = 0          
                            for yy in range (y, y+dx, 8):
                                for xx in range (x, x+dx, 8):
                                    bb,gg,rr=frameClone[y, x]
                                    if bb > 200 and gg < 50 and rr < 50:
                                        blueRate +=1
                                        #if enough color : positive detection
                                        if [blueRate>70]:
                                            cv2.rectangle(frameClone, (x,y), (x+dx,y+dx), red)
                                            #locate detection (left or right)
                                            if x<320 :
                                                oldManLeft +=1
                                            else :
                                                oldManRight +=1
                #green check (child)
                        if bl < 50 and gr > 200 and re < 50:
                        #take a square and check if blue
                            greenRate = 0          
                            for yy in range (y, y+dx, 8):
                                for xx in range (x, x+dx, 8):
                                    bb,gg,rr=frameClone[y, x]
                                    if bb < 50 and gg > 200 and rr < 50:
                                        greenRate +=1
                                        #if enough color : positive detection
                                        if [greenRate>70]:
                                            cv2.rectangle(frameClone, (x,y), (x+dx,y+dx), yellow)
                                            #locate detection (left or right)
                                            if x<320 :
                                                childLeft +=1
                                            else :
                                                childRight +=1
                #yellow check (animal)
                        if bl < 50 and gr > 200 and re > 200:
                        #take a square and check if blue
                            yellowRate = 0          
                            for yy in range (y, y+dx, 8):
                                for xx in range (x, x+dx, 8):
                                    bb,gg,rr=frameClone[y, x]
                                    if bb < 50 and gg > 200 and rr > 200:
                                        yellowRate +=1
                                        #if enough color : positive detection
                                        if [yellowRate>70]:
                                            cv2.rectangle(frameClone, (x,y), (x+dx,y+dx), blue)
                                            #locate detection (left or right)
                                            if x<320 :
                                                animalLeft +=1
                                            else :
                                                animalRight +=1
                #define left/right priority depending on person count and priority coefficient
                leftPriority = (manLeft*manCoeff)+(oldManLeft*oldManCoeff)+(childLeft*childCoeff)+(animalLeft*animalCoeff)
                rightPriority = (manRight*manCoeff)+(oldManRight*oldManCoeff)+(childRight*childCoeff)+(animalRight*animalCoeff)
                                
                #show left/right in green/red depending on priority
                if leftPriority < rightPriority:               
                    cv2.rectangle(frameClone, (10,10), (310,470), green)
                    cv2.rectangle(frameClone, (330,10), (650,470), red)
                elif rightPriority < leftPriority :
                    cv2.rectangle(frameClone, (10,10), (310,470), red)
                    cv2.rectangle(frameClone, (330,10), (650,470), green)
                    
            # analyze the line in the lower part of the image (y=400)
            # find the minimum and maximum values of the derivative
            d0=0
            minVal = 255
            maxVal = -255
            minPos = 0
            maxPos = 0
            for x in range(0, 640, 10):
                d = frameClone[400, x, 2]
 
                # find minimum and maximum change
                dif = int(d)-int(d0)
                d0 = d
                if dif < minVal and x != 0:
                    minVal = dif
                    minPos = x
                if dif > maxVal and x != 0:
                    maxVal = dif
                    maxPos = x         
                cv2.circle(frameClone, (x, 400-d), 5, red)
                cv2.circle(frameClone, (x, 400-dif), 3, blue)


            state = int((maxPos+minPos)/2)
            target = 320
            error = target-state
    
            steering = int(steeringGain * error)
            motorLeft.run(speed-steering, True)
            motorRight.run(speed+steering, True)
    
            cv2.line(frameClone, (maxPos, 0), (maxPos, 480), green)
            cv2.line(frameClone, (minPos, 0), (minPos, 480), green)

            cv2.line(frameClone, (0, 400), (640, 400), green)
            cv2.circle(frameClone, (target, 400), 50, green)
            
            #show camera
            cv2.imshow("Camera", frameClone)
            rawCapture.truncate(0)                    
            c = cv2.waitKey(1) & 0xFF
            
            #if color detected, quit image analysis
            if leftPriority > 10 or rightPriority > 10:
                break
            elif c==ord('r'): #reset color detection
                loop2 +=1 
                break
            
        #if left priority is bigger then car will go right
        if leftPriority < rightPriority:
            count=0
            while count<1000:
                motorLeft.run(speed, True)
                count = count + 0.3
                
        #if right priority is bigger then car will go left        
        elif rightPriority < leftPriority :
            count=0
            while count<1000:
                motorLight.run(speed/10, True)
                count = count + 0.1
        
        #stop color detection until reset
        colorDetection +=1
        print (colorDetection)
        
        c = cv2.waitKey(1) & 0xFF
        if c==ord('t'):#quit this loop
            loop2 +=1

c = cv2.waitKey(1) & 0xFF
if c == ord('p'): #stop everything
    loop +=1