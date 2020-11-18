import cv2
import numpy as np

np.random.seed(0)
img = np.random.randint(0, 100, (5, 5), np.unit8)
print('img =')
print(img)
kernel = np.random.randint(0,10, size=(3,3))*1/10
print('kernel =')
print(kernel)
output = cv2.filter2D(img, -1, kernel)
print('output =')
print(output)