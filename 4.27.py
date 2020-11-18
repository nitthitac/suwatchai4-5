import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image(BGRimage, windowName=None):
    img_RGB = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.figure(windowName)
    plt.imshow(img_RGB)

img = cv2.imread('D:/bookPic/tooDark.jpg')
img = img/255.0
gamma = [1, 0.5, 0.25, 0.125]
for g in gamma:
    result = np.unit8(pow(img,g)*255)
    show_image(result, 'Gamma={}'.format(g))
plt.show()