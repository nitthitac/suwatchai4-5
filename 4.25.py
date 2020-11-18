import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_gray(gray_img, windowName=None):
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

img = cv2.imread('D:/bookPic/gradientImage.jpg', 0)
show_gray(img, 'Original')
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
result = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 10)
show_gray(sobel_x, 'Sobel_x')
show_gray(sobel_y), 'Sobel_y'
show_gray(result, 'Combined Sobel')
plt.show()