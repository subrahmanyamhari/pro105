import cv2
import os

path = "album"
images = []


for i in os.listdir(path):
    images.append(i)
    print(i)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 0.5, (400,200))

for i in images:
    image = cv2.imread("album/"+i)
    image = cv2.resize(image,(400,200),3)
    print(image.shape)
    print(i)
    out.write(image)
    print(out)