import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img1 = cv2.imread('D:/bookPic/resize_brocooli.jpg')
img2 = cv2.imread('D:/bookPic/mixVeggies.jpg')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB.create()
kp1, des1 = sift.detectAndCompute(img1_gray, None)
kp2, des2 = sift.detectAndCompute(img2_gray, None)
matches = bf.knnMatch(des1, des2, k=2)
print(matches[0])
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
print('des1, des2, matches, good =', len(des1), len(des2), len(matches), len(good))
matching results = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
show_image(matching_result)
plt.show()