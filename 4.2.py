import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/bookpic/sky.jpg')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(1)
plt.imshow(img_RGB)
plt.figure(2)
color = ('b', 'g', 'r')
for chanel. col in zip(range(3), colors):
    hist_values = cv2.calcHist([img], channels=[channel], mask=none, histSize=[256], ranges[0, 256])
    plt.plot(hist_values, color=col)
plt.xlabel('Pixel Intesity')
plt.ylabel('No. of Pixels')
plt.xlim(0,256)
plt.ylim(0,2000)
plt.show()