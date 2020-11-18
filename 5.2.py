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

modes = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
         'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

tp = cv2.imread('D:/bookPic/reda_face.jpg',0)
w, h = tp.shape[::-1]
img = cv2.imread('D:/bookPic/reda6.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for m in modes:
    mode = eval(m)
    gray_copy = img_gray.copy()
    result = cv2.matchTemplate(gray_copy, tp, mode)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #extract the location of the object
    if mode in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    #draw a red rectangle on the found object in the image
    img_copy = img.copy()
    cv2.rectangle(img_copy, top_left, bottom_right, (0, 0, 255), 7)
    show_image(img_copy, m)
plt.show()