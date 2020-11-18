import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/bookPic/girl.jpg',0)

ret, otsu = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
mean_c = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 61, 5)
gaussian_c = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 71, 5)

#ploting the result
plt.figure('Original')
plt.imshow(img, cmap='gray')
plt.figure('Otsu')
plt.imshow(otsu, cmap=;'gray')
plt.figure('Gaussian_c')
plt.imshow(Gaussian_c, cmap=;'gray')
plt.show()