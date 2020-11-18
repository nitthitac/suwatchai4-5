import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_gray(gray_img, windowName)
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

img = cv2.imread('D:/bookPic/morphological.jpg', 0)
ret img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
show_gray(img, 'Original')
kernel = np.ones((3,3), np.unit8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1)
show_gray(gradient, 'Gradient')
plt.show()