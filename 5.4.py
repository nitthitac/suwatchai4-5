import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img = cv2.imread('D:/bookPic/block.jpg')
show_image(img, 'Input')
img gray = cv2.cvtColor(img. cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)
result = cv2.cornerHarris(img_gray, 2, 3, 0.04)
result = cv2.dilate(result, None, iterations=2)
img[result >= 0.01*result.max()] = [0,0,255]
show_image(img, 'Output')
plt.show()