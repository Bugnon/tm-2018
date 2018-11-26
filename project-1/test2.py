from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--trex.jpg", required = True,
help = "home/pi/tm-2018/images")
args = vars(ap.parse_args())

image = cv2.imread(args["trex.jpg"])
cv2.imshow("Original", image)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {255}, Green: {0}, Blue: {0}".format(r,
g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {255}, Green: {0}, Blue: {0}".format(r, g, b))