import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_gray(gray_img, windowName):
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

img = cv2.imread('D:/bookPic/morphological.jpg', 0)
ret img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
show_gray(img, 'Original')
kernel = np.ones((9,9), np.unit8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=3)
show_gray(opening, 'Opening')
plt.show()