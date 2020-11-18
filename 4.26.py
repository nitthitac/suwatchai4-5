import cv2
import matplotlib.pyplot as plt

def show_gray(gray_img, windowName=None):
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

img = cv2.imread('D:/bookPic/gradientImage.jpg', 0)
show_gray(img, 'Original')
lapacian = cv2.Lapacian(img, cv2.CV_64F, ksize=3)
show_gray(lapacian, 'Lapacian')
plt.show()