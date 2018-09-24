##import everything
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

##initialize camera (need to verify camera flip)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = True
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
pink = (255, 0, 255)
yellow = (255,255,0)
purple = (160,0,200)
##variable
x = 302
y = 206
r = 60

color = purple


##capture image
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    frame = f.array    
    frameClone = frame.copy()
    
    cv2.line(frameClone, (0,y),(640,y), green)
    cv2.line(frameClone, (x,0),(x,480), green)
    cv2. circle(frameClone, (x,y), r, green)

    print (frameClone[y+1,x+1])
    
        #take every pixel and check if red   
    for y in range (0, 640, 10):
        for x in range (0, 480, 10):
            bl,gr,re=frameClone[x,y]
            if bl<100 and gr<100 and re>150:
                #take a rectangle and check if red
                q = 0
                cv2.rectangle(frameClone, (x,y), (x+20,y+20), magenta)          
                for yy in range (y, y+20, 2):
                    for xx in range (x, x+20, 2):
                        bb,gg,rr=frameClone[x,y]
                        if [bb<100] and [gg<100] and [rr>150]:
                            q = q + 1
                            if [q>0]:
                                print ("man_detected")
        
    
    
    text = str(frameClone[y+1,x+1])
    org = (x,y)
    fontFace = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frameClone, text, org, fontFace, 2, color, 3)
    
    cv2.imshow("Camera", frameClone)
    rawCapture.truncate(0)
    
    c = cv2.waitKey(1) & 0xFF
    if c == ord('f'):  #quit
        break
    elif c == ord('w'):  #up
        y = y-10
    elif c == ord('s'):  #down
        y = y+10
    elif c == ord('a'):  #left
        x = x-10
    elif c == ord('d'):  #right
        x = x+10
    elif c == ord('q'):  #bigger
        r = r-5
    elif c == ord('e'):  #thiner
        r = r+5
    elif c == ord('u'):  #green
        color = green
    elif c == ord('i'):
        color = red
    elif c == ord('o'):
        color = blue
    elif c == ord('p') :
        break
    
        
