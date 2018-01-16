import cv2

path="../images/trex.png"

image=cv2.imread(path)

print("width: ", image.shape[1])
print("height: ", image.shape[0])
print("channels: ", image.shape[2])

cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)
