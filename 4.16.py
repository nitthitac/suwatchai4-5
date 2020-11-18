import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image(BGRimage, windowName):
    img_RGB = cv2.cv2Color(BGRimage, cv2.COLOR_BGR2RGB)
    plt.figure(windowName)
    plt.imshow(img_RGB)

img = cv2.imread('D:/bookPic/shapes.jpg',)
show_image(img, 'Original')
blurred = cv2.blur(img, (7,7))
show_image(blurred, 'Blurred with Average Blur')
plt.show()