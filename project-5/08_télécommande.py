import cv2
import nxt.locator
from nxt.motor import *
from nxt.sensor import *

b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_C)
m_right = Motor(b, PORT_A)
m_turn = Motor (b, PORT_B)

speed = 0

while True:
## c is the caracter read from the keyboard
    
    c = cv2.waitKey(50) & 0xFF
    print(c, speed)
    
    if c == ord('q'):  # quit
        break
    
    elif c == ord('w'): # increase speed
        speed = speed + 10
    
    elif c == ord('x'): # decrease speed
        speed = speed - 10
        
    elif c == ord('s'):  # stop
        speed = 0
    
    elif c == ord('a'): # turn left by 10 degrees and a speed of 50
        m_turn.turn(50, -10)

    elif c == ord('d'): # turn right by 10 degrees and a speed of 50
        m_turn.turn(50, 10)


##    adjust the speed parameter for both motors
    m_left.run(speed, True)
    m_right.run(speed, True)
    
print("quit")
    

        