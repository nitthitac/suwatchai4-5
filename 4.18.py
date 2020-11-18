import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image(BGRimage, windowName):
    img.RGB = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.figure(windowName)
    plt.imshow(img_RGB)

img = cv2.imread('D:/bookPic/shapes.jpg', 0)
show_image(img, 'Original')
blurred = cv2.medianBlur(img, 5)
show_image(blurred, 'Blurred with Median Blur')
plt.show()