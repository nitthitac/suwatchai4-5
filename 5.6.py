import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_gray(img, windowName=None):
    plt.figure(windowName)
    plt.imshow(img, cmap='gray')

img = cv2.imread('D:/bookPic/rada_face.jpg', 0)
img gray = cv2.blur(img_gray, (3,3))
show_image(img, 'Input')
#setting thresholds
median = np.median(img_gray)
min_th = int(max(0, 0.7*median))
max_th = int(min(255, 1.3*median))
print(median, min_th, max_th)
result = cv2.Canny(img_gray, min_th, max_th)
show_gray(result, 'Output')
plt.show()