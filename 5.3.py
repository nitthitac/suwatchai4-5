import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img = cv2.imread('D:/bookPic/abc.jpg')
show_image(img, 'Input')
img gray = cv2.cvtColor(img. cv2.COLOR_BGR2GRAY)
tp = cv2.imread('D:/bookPic/q.jpg',0)
w, h = tp.shape[::-1]

result = cv2.matchTemplate(img_gray,tp, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(result >= threshold)
for pt in  zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
show_image(img, str(threshold))
plt.show()