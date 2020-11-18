import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_gray(img, windowName=None):
    plt.figure(windowName)
    plt.imshow(img, cmap='gray')

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

tp = cv2.imread('D:/bookPic/reda_face.jpg',0)
w, h = tp.shape[::-1]
img = cv2.imread('D:/bookPic/reda6.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show_gray(tp, 'Template')
show_gray(img_gray, 'Image')
result = cv2.matchTemplate(img_gray, tp, cv2.TM_CCOEFF_NORMED)
show_gray(result, 'template matching')
#extract the location of the maximum value
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
#draw a red rectangle on the round object in the image
cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 7)
show_image(img, 'Output')
plt.show()