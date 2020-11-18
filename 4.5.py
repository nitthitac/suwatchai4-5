import cv2
import matplotlib.pyplot as plt

threshold = 200
maxValue = 255
threshold_type = cv2.THRESH_BINARY
img = cv2.imread('D:/bookPic/gradient.jpg',0)
plt.figure('Original')
plt.imshow(img, cmap='gray')
plt.figure('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('No. of Pixels')
plt.xlim(0,260)
plt.hist(img.ravel(), 256, [0,256])
ret,thresh = cv2.treshold(img, threshold, maxValue, threshold_type)
plt.figure('Thresholding')
plt.imshow(thresh, cmap='gray')
plt.show()