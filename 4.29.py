import cv2
import matplotlib.pyplot as plt

def show_gray(gray_img, windowName=None):
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

def show_image(BGRimage, windowName=None):
    img_RGB = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.figure(windowName)
    plt.imshow(img_RGB)

colors = ['b', 'g', 'r']
img = cv2.imread('D:/bookPic/tooDark.jpg')
plt.figure('Histogram')
for i,color in zip(range(3), colors):
    hist = cv2.calcHist(img, channels=[i], mask=None, histSize=[256],ranges=[0,256])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('No. of Pixels')
    plt.plot(hist, color = color)
show_image(img, 'Original')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:,:,2])
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
show_image(img_eq)
plt.figure('Histogram of Equalized')
for i, color in zip(range(3), colors):
    hist = cv2.calcHist(img_eq, channels=[i], mask=None,histSize=[256], ranges=[0,256])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('No. of Pixel')
    plt.plot(hist, color = color)
plt.show()