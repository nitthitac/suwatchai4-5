import cv2
import matplotlib.pyplot as plt

threshold = 250
maxValue = 255
img = cv2.imread ('D:/bookPic/alphabet.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure('Original')
plt.imshow(img_rgb)
plt.figure('img')
plt.imshow(img_gray, cmap='gray')
plt.figure('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('No. of Pixels')
plt.xlim(0,260)
plt.hist(img.ravel(), 256, [0,256])
ret,tresh = cv2.treshold(img_gray, threshold, maxValue,cv2.TRESH_BINARY)
plt.figure('Binary Thresholding')
plt.imshow(thresh, cmap='gray')
plt.show()