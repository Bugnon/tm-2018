#!/usr/bin/env python

import nxt.locator
from nxt.motor import *
from nxt.sensor import *

import time
from time import sleep

b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)

touch = Touch(b, PORT_1)
light = Light(b, PORT_2)
sound = Sound(b, PORT_3)
us = Ultrasonic(b, PORT_4)

print('Touch:', touch.get_sample())
print('Sound:', sound.get_sample())
print('Light:', light.get_sample())
print('Ultrasonic:', us.get_sample())

def spin_around(b):
    m_left.turn(50, 360)
    m_right.turn(100, 360)

##spin_around(b)

def tacho():
    print(m_left.get_tacho(), m_right.get_tacho())
    
def idle():
    m_left.idle()
    m_right.idle()
    print('idle')

def brake():
    m_left.brake()
    m_right.brake()
    print('brake')
    
tacho()
m_left.run(100)
m_right.run(100)
sleep(1)
brake()
tacho()

m_left.run(-100)
m_right.run(100)
sleep(1)
brake()
tacho()


##m.turn(100, 360)
##print(m.get_tacho())
##
##m.run(50)
##
##for i in range(5):
##    sleep(1)    
##    print(m.get_tacho())
##
##print('brake')
##m.brake()
##sleep(3)
##


