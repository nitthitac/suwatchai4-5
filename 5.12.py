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
orb = cv2.ORB_create()
mask = np.zeros(img2_gray.shape, np.uint8)
mask[255:, 190:390] = 255
kp_orb1, des1 = orb.detecAndCompute(img1_gray, None)
#replace 'mask' with None to detect keypoints for the whole image
kp_orb2, des2 = orb.detecAndCompute(img2_gray, mask)
print(len(kp_orb1), len(kp_orb2))
img_orb1 = cv2.drawKeypoints(img1, kp_orb1, img1, (255,0,0))
img_orb2 = cv2.drawKeypoints(img2, kp_orb2, img2, (255,0,0))
show_image(img_sift1, 'Resized Broccoli')
show_image(img_sift2, 'Original')
plt.show()