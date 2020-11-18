import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/bookpic/sky.jpg',0)
hist_values = cv2.calcHist([img], channels=[0], mask=none, histSize=[256], ranges=[0,256])
plt.xlabel('Pixel Intensity')
plt.ylabel('No. of Pixels')
#plot histrogram
plt.hist(img.reshape(-1), bins=256, range=[0,256], color='orange')
#plot the trend of pixel distribution
plt.plot(hist_value, color='k')
plt.show()