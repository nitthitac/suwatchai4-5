import cv2
import matplotlib.pyplot as plt

def show_gray(gray_img, windowName=None):
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

img = cv2.imread('D:/bookPic/gradientImage.jpg', 0)
show_gray(img, 'Original')
hist = cv2.calcHist(img, [0], None, [256], [0,256])
plt.figure('Histogram of Original')
plt.xlabel('Pixel Intensity')
plt.ylabel('No. of Pixels')
plt.hist(img.ravel(), 256, [0,256])
#histogram equalization
img eq = cv2.equalizeHist(img)
show_gray(img_eq, 'Equalized')
hist_eq = cv2.calcHist(img_eq, [0], None, [256], [0,256])
plt.figure('Histogram of Equalized')
plt.xlabel('Pixel Intensity')
plt.ylabel('No. of Pixels')
plt.hist(img_eq.ravel(), 256, [0,256])
plt.show()
