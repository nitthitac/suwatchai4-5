import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/bookpic/sky.jpg')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

plt.figure(1)
hist_values = cv2.calcHist([img_HSV], channels=[0, 11], mask=None,histSize=[180,255], ranges=[0, 181, 0, 256])
plt.xlabel('Hue')
plt.ylabel('Saturation')
plt.imshow(hist_values, interpolation = 'nearest')
plt.colorbar()
plt.figure(2)
hist_values = cv2.calcHist([img_HSV], channels=[0, 1], mask=None,histSize=[32,32], ranges=[0, 181, 0, 256])
plt.xlabel('Hue')
plt.ylabel('saturation')
plt.imshow(hist_values, interpolation = 'nearest')
plt.colorbar()
plt.show()
