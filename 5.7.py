import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_gray(img, windowName=None):
    plt.figure(windowName)
    plt.imshow(img, cmap='gray')

def show_gray(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img = cv2.imread('D:/bookPic/contours.jpg')
show_image(img, 'Input')
img gray = cv2.imread('D:/bookPic/contours.jpg', 0)
ret, thresh = cv2.threshold(img_gray, 0, 255,cv2.THRESH_BINARY+.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
output = np.zeros(img_gray.shape)
cv2.drawContours(output, contours, -1, 255)
show_gray(output, 'contours')
plt.show()