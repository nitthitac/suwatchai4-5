import cv2
import matplotlib.pyplot as plt

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

def show_gray(img, windowName=None):
    plt.figure(windowName)
    plt.imshow(img, cmap='gray')

img = cv2.imread('D:/bookPic/dice.jpg')
show_image(img, 'Input')
img gray = cv2.imread('D:/bookPic/dice.jpg', 0)
ret, thresh = cv2.threshold(img_gray, 0, 255,cv2.THRESH_BINARY+.THRESH_OTSU)
show_gray(thresh, 'Threshold')
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,255), 2)
show_image(img, 'contours')
print('hierarchy =')
print(hierarchy)
print('Total number of dice =', len(contours))
plt.show()