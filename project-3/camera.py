from picamera import PiCamera
from time import sleep

sleep(1)
camera = PiCamera()

camera.start_preview()
sleep(60)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

