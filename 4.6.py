import cv2
import matplotlib.pyplot as plt

house = cv2.imread('D:/bookPic/house.jpg', 0)
girl = cv2.imread('D:/bookPic/girl.jpg',0)

plt.figure('House')
plt.imshow(house, cmap='gray')
plt.figure('Histogram of the house')
plt.hist(house.ravel(), 256, (0,256))

plt.figure(('Girl'))
plt.imshow(girl, cmap='gray')
plt.figure('Histogram of the girl')
plt.hist(girl.ravel(), 256, (0,256))

#applying Otsu's binarization to both images
ret_H, thresh_H = cv2.threshold(house, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print('Otsu threshold-house =', ret_H)
plt.figure('Otsu-House')
plt.imshow(thresh_H, cmap='gray')
ret_G, thresh_G = cv2.threshold(house, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print('Otsu threshold-girl =', ret_G)
plt.figure('Otsu-Girl)
plt.imshow(thresh_G, cmap='gray')
plt.show()